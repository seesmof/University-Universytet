from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect

from .forms import MeasurementForm
from .models import Measurement


def measurements_list(req: HttpRequest):
    measurements = Measurement.objects.all()

    return render(req, "measurements/list.html", {"measurements": measurements})


def create_measurement(req: HttpRequest):
    if req.method == "POST":
        form = MeasurementForm(req.POST)
        if form.is_valid():
            print(form.cleaned_data)
            measurement = Measurement()
            measurement.value = form.cleaned_data["value"]
            measurement.description = form.cleaned_data["description"]
            measurement.save()
            return redirect("list")
    else:
        form = MeasurementForm()

    return render(req, "measurements/create.html", {"form": form})
