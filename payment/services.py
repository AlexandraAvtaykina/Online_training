import stripe

from config.settings import API_KEY_STRIPE
from payment.models import Payment


def create_payment(amount_payment, user):
    stripe.api_key = API_KEY_STRIPE

    payment_intent = stripe.PaymentIntent.create(
        amount=amount_payment,
        currency='usd',
        payment_method_types=['card'],
        description=f'Payment for {user}',
    )

    payment = Payment.objects.create(
        user=user,
        amount_payment=amount_payment,
        stripe_id=payment_intent.id
    )

    return payment


def retrieve(stripe_id):
    return stripe.PaymentIntent.retrieve(stripe_id)
