from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

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
            return redirect('home')

    form = TodoForm()

    return render(request, "todo/todo_add.html", {"form":form})    

def todo_delete(request, pk):
    todo = TodoModel.objects.filter(id=pk).first()

    if request.method == "POST":
        todo.delete()
        return redirect("home")
    
    return render(request, "todo/todo_delete.html", {"todo":todo})

def todo_update(request, pk):
    todo = TodoModel.objects.filter(id=pk).first()
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = TodoForm(request.POST or None, instance=todo)
    return render(request, "todo/todo_update.html", {"form":form})

def home(request):
    todos = TodoModel.objects.all()

    return render(request, "todo/todo_list.html", {"todos":todos})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})