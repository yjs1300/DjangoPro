from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("login",views.login),
    path("register",views.register),
    path("error",views.err),
    path("blank",views.blank),
    path("card",views.card),
    path("forgotpw",views.forgotpw),
    path("tables",views.tables),
    path("utilanimal",views.utilanimal),
    path("utilborder",views.utilborder),
    path("utilcolor",views.utilcolor),
    path("utilother",views.utilother),
    path("charts",views.charts),

    
]