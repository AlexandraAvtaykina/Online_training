import stripe
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from rest_framework.response import Response

from config.settings import API_KEY_STRIPE
from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'method_payment']  # Фильтрация по курсу или уроку и способу оплаты
    ordering_fields = ['date_of_payment']  # Сортировка по дате оплаты


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def create_payment(self, serializer):
        payment = serializer.save()
        stripe.api_key = API_KEY_STRIPE
        pay = stripe.PaymentIntent.create(
            amount=payment.amount_payment,
            currency="usd",
            automatic_payment_methods={"enabled": True},
        )
        pay.save()

        return super().perform_create(serializer)


class PaymentRetrieveView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get_payment(self, request, payment_id):
        stripe.api_key = API_KEY_STRIPE
        payment_retrieve = stripe.PaymentIntent.retrieve(
            payment_id,
        )

        return Response({
            "status": payment_retrieve.status,
            "body": payment_retrieve
        })
