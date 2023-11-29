from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("map", views.map, name="map"),
    path("admin", views.dash_admin, name="dash_admin"),

]
