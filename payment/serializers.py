from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from education.models import Course, Lesson
from payment.models import Payment
from payment.validators import PayValidator


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Payment """
    paid_course = SlugRelatedField(slug_field="title_course", queryset=Course.objects.all())
    paid_lesson = SlugRelatedField(slug_field="title_lesson", queryset=Lesson.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'  # Выводить все поля

        # Валидатор, который разрешает оплатить или курс, или урок
        validators = [PayValidator(field1='paid_course', field2='paid_lesson')]

