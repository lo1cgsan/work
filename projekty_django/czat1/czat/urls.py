from django.urls import path
from . import views

app_name = "czat"
urlpatterns = [
    path("", views.index, name="index"),
]