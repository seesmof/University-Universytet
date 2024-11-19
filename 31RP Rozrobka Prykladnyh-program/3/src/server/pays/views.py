from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from . import models
from .forms import Login

def index(request):
    return render(request,'login.html',{'form':Login()})