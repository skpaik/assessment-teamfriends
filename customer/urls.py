from django.urls import path

from .views import register_customer

urlpatterns = [
    path('customer/register', register_customer, name='register_customer'),
]
