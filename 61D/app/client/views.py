from django.http import HttpRequest
from django.shortcuts import render
from django.views.generic import ListView

from .models import Task


# Create your views here.
def index(request: HttpRequest):
    context = dict()
    return render(request, "client/index.html", context)


class TasksList(ListView):
    model = Task
