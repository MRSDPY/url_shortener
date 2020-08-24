from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("ip/", views.ip, name="ip"),
    path("short/", views.shortener, name="short"),
    url(r"^(?P<shortener>[\w-]+)/$", views.redirect, name="redirect"),
]
