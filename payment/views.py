import stripe
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, get_object_or_404
from rest_framework.response import Response

from config.settings import API_KEY_STRIPE
from payment.models import Payment
from payment.serializers import PaymentSerializer
from payment.services import create_payment


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'method_payment']  # Фильтрация по курсу или уроку и способу оплаты
    ordering_fields = ['date_of_payment']  # Сортировка по дате оплаты


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount_payment = serializer.validated_data.get('amount_payment')
        user = self.request.user
        payment = create_payment(amount_payment, user)
        response_data = {
            "id": payment.id,
            "payment_amount": payment.amount_payment
        }
        headers = self.get_success_headers(serializer.data)

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)


class PaymentRetrieveAPIView(RetrieveAPIView):
    serializer_class = PaymentSerializer

    def get(self, request, pk):
        payment = get_object_or_404(Payment, pk=pk)
        stripe_id = payment.stripe_id
        stripe.api_key = API_KEY_STRIPE
        payment_intent = stripe.PaymentIntent.retrieve(stripe_id)

        return Response(payment_intent, status=status.HTTP_200_OK)
