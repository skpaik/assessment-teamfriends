import random

from django.utils import timezone

from birthdaywish.tasks import send_birthday_emails
from customer.models import Customer


def cron_1():
    send_birthday_emails()
