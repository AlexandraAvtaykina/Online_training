from django.urls import path
from rest_framework.routers import DefaultRouter

from education.apps import EducationConfig
from education.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
  LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = EducationConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [

  path('lesson_list/', LessonListAPIView.as_view(), name='lesson_list'),  # Список уроков
  path('lesson_retrieve/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),  # Детальная информация по уроку
  path('lesson_create/create/', LessonCreateAPIView.as_view(), name='lesson_create'),  # Создание урока
  path('lesson_update/<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),  # Редактирование урока
  path('lesson_destroy/<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),  # Удаление урока
  path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='subscription_create'),  # Создание подписки
  path('subscription_destroy/<int:pk>/', SubscriptionDestroyAPIView.as_view(), name='subscription_destroy'),  # Удаление подписки

] + router.urls   # Присоединяем курсы
