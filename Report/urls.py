from django.urls import path
from Report import views

urlpatterns = [
    path("report/", views.report),
]