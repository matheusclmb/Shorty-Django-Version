from django.urls import path

from . import views

appname = "shortener"

urlpatterns = [
    path("", views.home, name="home"),
    path("<str:shortened_path>", views.redirect_url_view, name="redirect"),
]
