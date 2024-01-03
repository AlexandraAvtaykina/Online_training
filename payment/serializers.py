from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson
from payment.models import Payment
from payment.validators import PayValidator


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Payment """

    class Meta:
        model = Payment
        fields = "__all__"
        validators = [PayValidator(field1='paid_course', field2='paid_lesson')]

