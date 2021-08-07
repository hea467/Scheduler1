from django.urls import path
from . import views

app_name = "project"

urlpatterns = [
    path("", views.index, name="index"),
    path("main/", views.main, name="main"),
    path("new_event", views.new_event, name="new_event"),
    path("listevents/", views.listevents, name="listevents"),
    path("blog/", views.blog, name="blog"),
    path("newblog/", views.newblog, name="newblog"),
    path("delete/", views.delete, name="delete"),
    path("editevent/<int:event_id>/", views.editevent, name="editevent"),
    path("deleteevent/<int:event_id>/", views.deleteevent, name="deleteevent"),
]
