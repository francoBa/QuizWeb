from django.urls import path
from . import views

urlpatterns = [
  path("", views.inicio, name="inicio"),
  path("play/", views.jugar, name="play"),
  path("index2/", views.index2, name="index2"),
]
