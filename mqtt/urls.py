from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.index, name="index"),
    path("admin", views.dash_admin, name="dash_admin"),
    path("team-view", views.team_view, name="team_view"),
    path("login", views.login_view, name="login"),

    #conceptual ideation for team dash
    path("test/map", views.map, name="map"),
    path("test/chart", views.chart, name="chart"),

]
