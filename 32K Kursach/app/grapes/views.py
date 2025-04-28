from django.http import HttpResponse
from django.shortcuts import render

from grapes.models import Bunch

# Create your views here.
def index(request):
    all_bunches=Bunch.objects.all()
    return render(request, "index.html", {"bunches": all_bunches})

def bunches(request, id):
    return HttpResponse(id)

def new_bunch(request):
    return HttpResponse('Fill in')