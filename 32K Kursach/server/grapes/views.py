from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from grapes.forms import BunchForm
from grapes.models import Bunch
from grapes.utils import process_bunch, visualize_bunch

@login_required
def profile(request):
    user=request.user
    bunches=Bunch.objects.filter(owner=request.user)
    return render(request, "profile.html", {"user": user, "bunches": bunches})

def index(request):
    all_bunches=list()
    if request.user.is_authenticated:
        all_bunches=Bunch.objects.filter(owner=request.user)
        for bunch in all_bunches:
            processed_bunch=process_bunch(bunch)
            bunch.stage=processed_bunch.stage
            bunch.save()
    return render(request, "index.html", {"bunches": all_bunches, "user": request.user})

@login_required
def bunch(request, id):
    bunch=Bunch.objects.get(pk=id)
    visual_bunch=visualize_bunch(bunch)
    return render(request, "bunch.html", {"bunch": visual_bunch})

@login_required
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
            processed_bunch.save()
            # add owner
            bunch.owner.add(request.user)
            processed_bunch.save()
            return HttpResponseRedirect(f'/bunch/{processed_bunch.id}')
    else:
        form=BunchForm()

    return render(request,"new_bunch.html",{"form":form})
