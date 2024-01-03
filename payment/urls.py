from django.urls import path

from payment.apps import PaymentConfig
from payment.views import PaymentCreateAPIView

app_name = PaymentConfig.name

urlpatterns = [
  path('create/', PaymentCreateAPIView.as_view(), name='payment_create'),  # Создание платежа
]
