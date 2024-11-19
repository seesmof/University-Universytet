from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from . import models

def index(request):
    return HttpResponse(settings.CURRENT_USER_ID)