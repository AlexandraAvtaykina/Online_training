from django.core.management import BaseCommand

from payment.models import Payment


class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        payment = Payment.objects.create(
            date_of_payment='2023-09-11',
            amount_payment=90000,
            method_payment='cash'
        )

        payment.save()
