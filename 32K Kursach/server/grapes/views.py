from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from grapes.forms import BunchForm
from grapes.models import Bunch
from grapes.serializers import BunchSerializer
from grapes.utils import process_bunch, visualize_bunch

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

@csrf_exempt
def bunches_list(request):
    if request.method=='GET':
        bunches=Bunch.objects.all()
        serializer=BunchSerializer(bunches,many=True)
        return JsonResponse(serializer.data,safe=False)

    elif request.method=='POST':
        data=JSONParser().parse(request)
        serializer=BunchSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors,status=400)