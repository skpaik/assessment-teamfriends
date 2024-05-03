# tasks.py in your Django app
from django.utils import timezone

from customer.models import Customer
from .utils import simulated_send_email  # This function simply prints the email details


def send_birthday_emails():
    print(f"Sending email start")

    today = timezone.now().date()
    current_year = today.year

    # birthdays_today = Customer.objects.filter(birthday__month=today.month, birthday__day=today.day)
    birthdays_today = Customer.objects.all()

    for customer in birthdays_today:
        subject = "Happy Birthday!"
        message = f"Dear {customer.name},\nWe wish you a very Happy Birthday!"
        simulated_send_email(customer.email, subject, message)

        # Update wish_year to current_year
        customer.wish_year = current_year
        customer.save()

    print(f"Sending email end")
