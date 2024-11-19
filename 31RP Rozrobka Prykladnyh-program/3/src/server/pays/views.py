from django.shortcuts import render
from django.http import HttpResponse

from . import models

def index(request):
    from django.conf import settings
    return HttpResponse(settings.CURRENT_USER_ID)