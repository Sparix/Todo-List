from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic

from .models import Task, Tags


# Create your views here.


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TagsListView(generic.ListView):
    model = Tags


class CreateTaskView(generic.CreateView):
    model = Task
    success_url = reverse_lazy("tasks:home-page")
    fields = "__all__"


class CreateTagView(generic.CreateView):
    model = Tags
    success_url = reverse_lazy("tasks:tags-list")
    fields = "__all__"


class UpdateTaskView(generic.UpdateView):
    model = Task
    success_url = reverse_lazy("tasks:home-page")
    fields = "__all__"


class UpdateTagView(generic.UpdateView):
    model = Tags
    success_url = reverse_lazy("tasks:tags-list")
    fields = "__all__"


def change_status_tasks(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_completed:
        task.is_completed = False
    else:
        task.is_completed = True
    task.save()
    return redirect("tasks:home-page")


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("tasks:home-page")


class DeleteTagsView(generic.DeleteView):
    model = Tags
    success_url = reverse_lazy("tasks:tags-list")
