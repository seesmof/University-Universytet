from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from grapes.forms import BunchForm
from grapes.models import Bunch
from grapes.utils import process_bunch

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
            data=form.cleaned_data
            # create object
            bunch=Bunch(
                count=data['count'],
                outside=data['outside'],
                sugar=data['sugar'],
                shape=data['shape'],
                color=data['color'],
            )
            # process data and make stage
            processed_bunch=process_bunch(bunch)
            print(processed_bunch.stage)
            return HttpResponseRedirect('/')
    else:
        form=BunchForm()

    return render(request,"new_bunch.html",{"form":form})