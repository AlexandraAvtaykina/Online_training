from django.db import models

from education.models import Lesson, Course, NULLABLE
from users.models import User


class Payment(models.Model):
    PAY_CARD = 'card'
    PAY_CASH = 'cash'

    PAY_TYPES = (
        (PAY_CASH, 'наличные'),
        (PAY_CARD, 'перевод')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь', **NULLABLE)
    date_of_payment = models.DateField(verbose_name='дата оплаты')
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='оплаченный курс', **NULLABLE)
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='оплаченный урок', **NULLABLE)
    amount_payment = models.PositiveIntegerField(verbose_name='сумма оплаты', **NULLABLE)
    method_payment = models.CharField(max_length=20, choices=PAY_TYPES, verbose_name='способ оплаты')

    def __str__(self):
        return f'{self.paid_course if self.paid_course else self.paid_lesson} - {self.amount_payment}'

    class Meta:
        verbose_name = 'платеж'
        verbose_name_plural = 'платежи'

