from birthdaywish.tasks import send_birthday_emails


def cron_1():
    send_birthday_emails()
