from rest_framework.exceptions import ValidationError


class PayValidator:
    """ Класс валидатора, который проверяет, что оплачиваться будет или курс, или урок """
    def __init__(self, field1, field2):
        self.field1 = field1
        self.field2 = field2

    def __call__(self, value):
        pay_course = dict(value).get(self.field1)
        pay_lesson = dict(value).get(self.field2)

        if (pay_course is None and pay_lesson is None) or (pay_course is not None and pay_lesson is not None):
            raise ValidationError('Можно оплатить или курс, или урок')
