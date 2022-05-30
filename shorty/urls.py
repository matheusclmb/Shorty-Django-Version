from django.urls import path
from rest_framework import routers

from . import views

appname = "shortener"
router = routers.DefaultRouter()
router.register(r"shortener", views.ShortenerViewSet, basename="Shortener")
router.register(r"stats", views.StatsSerializer, basename="Shortener")

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:shortened_path>", views.redirect_url_view, name="redirect"),
    path(
        "api/shorten/<str:shortcode>",
        views.ShortenerViewSet.as_view({"get": "list"}),
        name="shortener",
    ),
    path(
        "api/stats/<str:shortcode>",
        views.StatsViewSet.as_view({"get": "list"}),
        name="stats",
    ),
]
