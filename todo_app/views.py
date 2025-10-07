from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all().order_by("created_at")
    return render(request, "todo_app/index.html", {"todos": todos})


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        if title:
            Todo.objects.create(title=title)

    todos = Todo.objects.all().order_by("created_at")
    return render(request, "todo_app/partials/_todo_list.html", {"todos": todos})


def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.completed = not todo.completed
    todo.save()

    # Kirim kembali hanya item yang diperbarui sebagai partial
    return render(request, "todo_app/partials/_todo_item.html", {"todo": todo})


def delete_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse(status=200)
