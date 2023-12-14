from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView

from payment.models import Payment
from payment.serializers import PaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'method_payment']  # Фильтрация по курсу или уроку и способу оплаты
    ordering_fields = ['date_of_payment']  # Сортировка по дате оплаты
