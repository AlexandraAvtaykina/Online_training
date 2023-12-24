from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentListView, PaymentCreateView, PaymentRetrieveView

app_name = PaymentConfig.name

urlpatterns = [
  path('list/', PaymentListView.as_view(), name='payment_list'),  # Список платежей
  path('create/', PaymentCreateView.as_view(), name='payment_create'),  # Создание платежа
  path('retrieve/<int:pk>/', PaymentRetrieveView.as_view(), name='payment_retrieve'),  # Создание платежа
]
