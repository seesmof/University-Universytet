from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET','POST'])
def bunches_list(request, format=None):
    if request.method=='GET':
        bunches=Bunch.objects.all()
        serializer=BunchSerializer(bunches,many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=BunchSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET','PUT','DELETE'])
def bunch_detail(request, pk, format=None):
    try:
        bunch=Bunch.objects.get(pk=pk)
    except Bunch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=='GET':
        serializer=BunchSerializer(bunch)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer=BunchSerializer(bunch,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    if request.method=='DELETE':
        bunch.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)