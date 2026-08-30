from django.http import HttpRequest
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from django.conf import settings
from .models import Measurement


def index_view(req: HttpRequest):
    return redirect("list")


def measurements_list(req: HttpRequest):
    measurements = Measurement.objects.all()

    return render(req, "measurements/list.html", {"measurements": measurements})


def measurement_details(req: HttpRequest, id: int):
    measurement = Measurement.objects.get(pk=id)

    return render(req, "measurements/details.html", {"measurement": measurement})


class CreateMeasurement(generic.CreateView):
    model = Measurement
    fields = "__all__"
    success_url = "/list"


class ListMeasurements(generic.ListView):
    model = Measurement


class MeasurementDetails(generic.DetailView):
    model = Measurement
