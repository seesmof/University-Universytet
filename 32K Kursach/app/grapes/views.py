from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView

from grapes.forms import BunchForm
from grapes.models import Bunch

# Create your views here.
def index(request):
    all_bunches=Bunch.objects.all()
    return render(request, "index.html", {"bunches": all_bunches})

def bunches(request, id):
    return HttpResponse(id)

def new_bunch(request):
    if request.method=="POST":
        form=BunchForm(request.POST)
        if form.is_valid():
            return redirect(index)
    else:
        form=BunchForm()

    return render(request,"new_bunch.html",{"form":form})