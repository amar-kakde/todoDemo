from django.urls import path
from . import views

urlpatterns = [
    path("", view=views.index, name="index"),
    path("home/", view=views.home, name="home"),
    path("add/", view=views.todo_add, name='todo_add'),
    path("delete/<int:pk>/", view=views.todo_delete, name="todo_delete"),
    path("update/<int:pk>/", view=views.todo_update, name="todo_update"),
]
