from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("ajax_speed", views.ajax_speed, name="ajax_speed"),
    path("map", views.map, name="map"),

]
