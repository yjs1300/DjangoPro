from django.urls import path
from . import views

urlpatterns = [
    path("map/", views.showmap),
    path("submap/", views.rental),
    path("submap2/", views.rental),
    path("chart/", views.chart),
]