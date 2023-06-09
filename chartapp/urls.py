from django.urls import path
from . import views

urlpatterns = [
    path("charthome/", views.charthomeFunc),
]