from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework import viewsets

from education.models import Course, Lesson, Subscription
from education.paginations import LessonPaginator
from education.permissions import IsAutor, IsManager
from education.serializers import CourseSerializer, LessonSerializer, CourseCreateSerializer, SubscriptionSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """ Простой ViewSet-класс для вывода информации """
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = LessonPaginator

    """ Функция привязывает автора к его курсу"""
    def perform_create(self, serializer):
        # привязка создателя к курсу
        serializer.save()
        self.request.user.course_set.add(serializer.instance)

    """ Если юзер не модератор, функция показывает только его курсы"""
    def get_queryset(self):
        if not self.request.user.is_staff:
            return Course.objects.filter(autor=self.request.user)
        elif self.request.user.is_staff:
            return Course.objects.all()


class LessonListAPIView(ListAPIView):
    """ Отвечает за отображение списка сущностей (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsAutor]
    pagination_class = LessonPaginator


class LessonRetrieveAPIView(RetrieveAPIView):
    """ Отвечает за отображение одной сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsAutor]


class LessonCreateAPIView(CreateAPIView):
    """ Отвечает за создание сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager | IsAutor]

    """ Функция привязывает автора к его уроку"""
    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.author = self.request.user
        new_lesson.save()


class LessonUpdateAPIView(UpdateAPIView):
    """ Отвечает за редактирование сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAutor]


class LessonDestroyAPIView(DestroyAPIView):
    """ Отвечает за удаление сущности (Generic-класс)"""

    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsManager]


class SubscriptionCreateAPIView(CreateAPIView):
    """ Отвечает за создание сущности (Generic-класс) Подписка"""

    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]

    """ Функция ставит True, если пользователь подписался на курс"""
    def perform_create(self, serializer):
        serializer.save()
        self.request.user.subscription_set.add(serializer.instance)


class SubscriptionDestroyAPIView(DestroyAPIView):
    """ Отвечает за удаление сущности (Generic-класс) Подписка"""

    queryset = Subscription.objects.all()
    permission_classes = [IsManager | IsAutor]
