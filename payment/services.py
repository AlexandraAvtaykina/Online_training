import stripe

from payment.models import Payment


def get_pay(amount_payment, user):
    stripe.api_key = 'sk_test_51OPrL0FA8bwzNlKAccboalFsU9PMecDMNqw0AmTAGCSkgKlXbZF3ssokVNU71gSutkFYzjcamxD5X1s3dlSWTjOe00CRoKBFAa'
    pay = stripe.PaymentIntent.create(
        amount=amount_payment,
        currency="usd",
        automatic_payment_methods={"enabled": True}
    )

    payment = Payment.objects.create(
        user=user,
        amount_payment=amount_payment,
        stripe_id=pay.id
    )

    return payment
