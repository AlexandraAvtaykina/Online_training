import stripe
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'method_payment']  # Фильтрация по курсу или уроку и способу оплаты
    ordering_fields = ['date_of_payment']  # Сортировка по дате оплаты


class PaymentCreateAPIView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        payment = serializer.save()
        self.request.user.payment_set.add(serializer.instance)
        pay = stripe.PaymentIntent.create(
            amount=payment.amount_payment,
            currency="usd",
            automatic_payment_methods={"enabled": True}
        )
        pay.save()
        return super().perform_create(serializer)

