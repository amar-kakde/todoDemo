from django.shortcuts import redirect, render

from .models import TodoModel
from .forms import TodoForm

# Create your views here.

def index(request):
    todos = TodoModel.objects.all()

    return render(request, "todo/index.html", {"todos":todos})

def todo_add(request):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    form = TodoForm()

    return render(request, "todo/todo_add.html", {"form":form})    

def todo_delete(request, pk):
    todo = TodoModel.objects.filter(id=pk)

    if request.method == "POST":
        todo.delete()
        return redirect("home")
    
    return render(request, "todo/todo_delete.html", {"todo":todo})

def todo_update(request, pk):
    if request.method == "POST":
        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")

    todo = TodoModel.objects.filter(id=pk).first()
    form = TodoForm(request.POST or None, instance=todo)

    return render(request, "todo/todo_update.html", {"form":form})

def todo_list(request):
    pass


