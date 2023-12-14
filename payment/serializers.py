from rest_framework import serializers

from payment.models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Payment """
    class Meta:
        model = Payment
        fields = '__all__'  # Выводить все поля
