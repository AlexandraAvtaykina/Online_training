from django.db import models

from users.models import User

NULLABLE = {'blank': 'True', 'null': 'True'}


class Course(models.Model):
    title_course = models.CharField(max_length=50, verbose_name='название курса')
    image_course = models.ImageField(upload_to='course/', verbose_name='картинка курса', **NULLABLE)
    description_course = models.TextField(verbose_name='описание курса')

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title_course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=50, verbose_name='название урока')
    description_lesson = models.TextField(verbose_name='описание урока')
    image_lesson = models.ImageField(upload_to='lesson/', verbose_name='картинка урока', **NULLABLE)
    url_lesson = models.URLField(verbose_name='ссылка на видео', **NULLABLE)
    url_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='ссылка на курс', **NULLABLE)

    author = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE)

    def __str__(self):
        return f'{self.title_lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
