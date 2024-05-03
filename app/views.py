from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone

@api_view(['GET'])
def home_page(request):
    res = {
        "Message": "Please open the readme.md file for details instructions",
        "time": timezone.now()
    }
    return Response(res, status=status.HTTP_200_OK)
