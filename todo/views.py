from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm

from .models import TodoModel
from .forms import TodoForm, CustomUserCreationForm

# Create your views here.

def index(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")

    form = AuthenticationForm()    
    return render(request, "todo/index.html", {"form":form})

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
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'your account has been created successfully.')
            return redirect("home")
        else:
            messages.error(request, 'please correct the errors below')

    form = CustomUserCreationForm()

    return render(request, "registration/signup.html", {"form":form})