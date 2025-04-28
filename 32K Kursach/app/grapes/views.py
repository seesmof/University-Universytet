from django.http import HttpResponse
from django.shortcuts import render

from grapes.models import Bunch

# Create your views here.
def index(request):
    all_bunches=Bunch.objects.all()
    res=', '.join([str(b) for b in all_bunches])
    return render(request, "index.html", bunches=res)