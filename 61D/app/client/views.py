from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Task


# Create your views here.
def index(request: HttpRequest):
    context = dict()
    return render(request, "client/index.html", context)


class TaskList(ListView):
    model = Task


class TaskCreate(CreateView):
    model = Task
    fields = "__all__"
    success_url = "task/"
