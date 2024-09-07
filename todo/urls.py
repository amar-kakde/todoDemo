from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("home/", view=views.index, name="home"),
    path("add/", view=views.todo_add, name='todo_add'),
    path("delete/", view=views.todo_delete, name="todo_delete"),
    path("update", view=views.todo_update, name="todo_update"),
]
