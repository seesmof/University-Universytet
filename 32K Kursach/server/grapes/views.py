from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework import permissions,viewsets
from django.contrib.auth.models import Group,User

from grapes.forms import BunchForm
from grapes.models import Bunch
from grapes.serializers import GroupSerializer, UserSerializer
from grapes.utils import process_bunch, visualize_bunch

# Create your views here.
def index(request):
    all_bunches=Bunch.objects.all()
    for bunch in all_bunches:
        processed_bunch=process_bunch(bunch)
        bunch.stage=processed_bunch.stage
        bunch.save()
    return render(request, "index.html", {"bunches": all_bunches})

def bunch(request, id):
    bunch=Bunch.objects.get(pk=id)
    visual_bunch=visualize_bunch(bunch)
    return render(request, "bunch.html", {"bunch": visual_bunch})

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
            return HttpResponseRedirect(f'/bunch/{processed_bunch.id}')
    else:
        form=BunchForm()

    return render(request,"new_bunch.html",{"form":form})

class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializer
    permission_classes=[permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    queryset=Group.objects.all().order_by('name')
    serializer_class=GroupSerializer
    permission_classes=[permissions.IsAuthenticated]