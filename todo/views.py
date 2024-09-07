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

def todo_delete(request):
    pass


def todo_update(request):
    pass


def todo_list(request):
    pass


