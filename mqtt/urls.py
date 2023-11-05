from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("ajax_speed", views.ajax_speed, name="ajax_speed"),
    path("ajax_location", views.ajax_location, name="ajax_location"),
    path("ajax_battery", views.ajax_battery, name="ajax_battery"),
    path("map", views.map, name="map"),

]
