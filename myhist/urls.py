from django.urls import path
from myhist import views

urlpatterns = [
    path("", views.myhistFunc),
    path("save", views.histSaveFunc),
    path("history", views.histFunc),
    path("histchart",views.chartFunc),
]