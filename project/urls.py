from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.main, name="main"),
    path("new_event", views.new_event, name="new_event"),
]
