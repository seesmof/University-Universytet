import os
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic

from django.conf import settings
from .forms import MeasurementForm
from .models import Measurement


def measurements_list(req: HttpRequest):
    measurements = Measurement.objects.all()

    return render(req, "measurements/list.html", {"measurements": measurements})


def create_measurement(req: HttpRequest):
    if req.method == "POST":
        form = MeasurementForm(req.POST)
        if form.is_valid():
            measurement = Measurement()
            measurement.value = form.cleaned_data["value"]
            measurement.description = form.cleaned_data["description"]
            measurement.save()
            return redirect("list")
    else:
        form = MeasurementForm()

    return render(req, "measurements/create.html", {"form": form})


def index_view(req: HttpRequest):
    return redirect("list")


def measurement_details(req: HttpRequest, id: int):
    measurement = get_object_or_404(Measurement, pk=id)

    return render(req, "measurements/details.html", {"measurement": measurement})
