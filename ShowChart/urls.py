from django.urls import path
from . import views

app_name = "ShowChart"

urlpatterns = [
    path("", views.index),
    path("login",views.login),
    path("register",views.register),
    path("error",views.err),
    path("cards",views.card),
    path("forgotpw",views.forgotpw),
    path("charts",views.charts),
]