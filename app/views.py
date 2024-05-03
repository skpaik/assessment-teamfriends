from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
import logging


logger = logging.getLogger(__name__)
# from birthdaywish.tasks import send_birthday_emails
@api_view(['GET'])
def home_page(request):
    res = {
        "Message": "Please open the readme.md file for details instructions",
        "time": timezone.now()
    }
    logger.info(res)
    logger.debug("my_scheduled_job running res")
    # send_birthday_emails()
    return Response(res, status=status.HTTP_200_OK)
