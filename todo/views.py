from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import TodoModel
from .forms import TodoForm

# Create your views here.

def index(request):
    return render(request, "todo/index.html", {})

@login_required
def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('home')

    form = TodoForm()

    return render(request, "todo/todo_add.html", {"form":form})    

@login_required
def todo_delete(request, pk):
    todo = TodoModel.objects.filter(id=pk).first()

    if request.method == "POST":
        todo.delete()
        return redirect("home")
    
    return render(request, "todo/todo_delete.html", {"todo":todo})

@login_required
def todo_update(request, pk):
    todo = TodoModel.objects.filter(id=pk).first()
    
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect("home")

    form = TodoForm(request.POST or None, instance=todo)
    return render(request, "todo/todo_update.html", {"form":form})

@login_required
def home(request):
    todos = TodoModel.objects.filter(user=request.user)

    return render(request, "todo/home.html", {"todos":todos})


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'your account has been created successfully.')
            return redirect("login")

    form = UserCreationForm()

    return render(request, "registration/signup.html", {"form":form})