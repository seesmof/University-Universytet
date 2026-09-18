from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.
def index(request: HttpRequest):
    context = dict()
    return render(request, "client/index.html", context)
