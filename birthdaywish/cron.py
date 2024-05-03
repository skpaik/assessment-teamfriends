import random

from django.utils import timezone

from customer.models import Customer


def print_hello():
    print("Hello")
    number = random.randint(0, 100).__str__()

    Customer.objects.create(name="Abul Mal" + number,
                            email=number + "email@gmail.com",
                            birthday=timezone.now(),
                            wish_year=7 + int(number)
                            )
