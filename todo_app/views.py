from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Todo

# Create your views here.


def index(request):
    todos = Todo.objects.all().order_by("created_at")
    return render(request, "todo_app/index.html", {"todos": todos})


def get_todo_item(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    return render(request, "todo_app/partials/_todo_item.html", {"todo": todo})


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
    return render(request, "todo_app/partials/_todo_item.html", {"todo": todo})


def delete_todo(_, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()

    return HttpResponse(status=200)


def edit_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == "POST":
        todo.title = request.POST.get("title", "")
        todo.save()

        return render(request, "todo_app/partials/_todo_item.html", {"todo": todo})

    return render(request, "todo_app/partials/_edit_form.html", {"todo": todo})
