# todo_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add-todo/", views.add_todo, name="add_todo"),
    path("update-todo/<int:pk>/", views.update_todo, name="update_todo"),
    path("delete-todo/<int:pk>/", views.delete_todo, name="delete_todo"),
]
