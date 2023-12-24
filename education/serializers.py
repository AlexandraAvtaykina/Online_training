from rest_framework import serializers

from education.models import Course, Lesson, Subscription
from education.validators import UrlValidator
from payment.services import get_url


class SubscriptionSerializer(serializers.ModelSerializer):
    """ Сериализатор модели подписки"""

    class Meta:
        model = Subscription
        fields = '__all__'


class LessonCourseSerializer(serializers.ModelSerializer):
    """ Cериализатор для модели Course, который будет включать данные об уроках """

    class Meta:
        model = Lesson
        fields = ('pk', 'title_lesson',)


class CourseCreateSerializer(serializers.ModelSerializer):
    """ Сериализатор для создания Course"""

    class Meta:
        model = Course
        fields = ('title_course', 'description_course',)


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Course"""

    lesson_count = serializers.IntegerField(source='lesson_set.all.count', read_only=True)  # поле вывода количества уроков
    lessons = LessonCourseSerializer(source='lesson_set', read_only=True, many=True)  # поле вывода уроков
    course_subscription = serializers.SerializerMethodField()  # поле подписки на курс
    url_payment = serializers.SerializerMethodField()  # поле ссылки на оплату

    def get_url_payment(self, obj):
        """ Метод вывода ссылки на оплату курса """
        return get_url(obj)

    def get_course_subscription(self, obj):
        """ Метод вывода подписан ли пользователь на курс """
        return Subscription.objects.filter(course_subscription=obj, user=self.context['request'].user).exists()

    def get_lesson_count(self, instance):
        """ Метод вывода количества уроков """
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = ('pk', 'title_course', 'image_course', 'description_course', 'lesson_count', 'lessons',
                  'course_subscription', 'url_payment',)


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор модели Lesson """

    class Meta:
        model = Lesson
        fields = '__all__'  # Выводить все поля
        validators = [UrlValidator(field='url_lesson')]
