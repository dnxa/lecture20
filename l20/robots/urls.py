from django.urls import path
from .views import robot_form_request

urlpatterns = [
    path('', robot_form_request, name="robot_form_request")
]