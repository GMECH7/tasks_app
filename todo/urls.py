from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create-task/", views.createTask, name="create-task"),
]
