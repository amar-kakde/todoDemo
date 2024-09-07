from django.shortcuts import render

from .models import TodoModel
from .forms import TodoForm

# Create your views here.

def index(request):
    return render(request, "todo/index.html", {})

def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()

    form = TodoForm()

    return render(request, "todo/todo_add.html", {"form":form})    

def todo_delete(request):
    pass


def todo_update(request):
    pass


def todo_list(request):
    pass


