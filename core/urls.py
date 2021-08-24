from django.urls import path
from . import views


urlpatterns = [
  path("", views.inicio, name="inicio"),
  path("compartir/", views.compartir, name="compartir"),
  path("jugar/", views.jugar, name="jugar"),
  path("index2/", views.index2, name="index2"),
]
