import os
from typing import Any

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
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


class MeasurementList(generic.ListView):
    model = Measurement
    context_object_name = "measurements"
    template_name = "measurements/list.html"

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        try:
            file_path: str = os.path.join(settings.BASE_DIR, "test_data.txt")
            with open(file_path, encoding="utf-8", mode="r") as f:
                lines = f.readlines()
            for value in lines:
                print(value)
                Measurement.objects.get_or_create(value=value)
        except IOError:
            print("ERROR: Couldn't read the file.")
            pass

        return super(MeasurementList, self).get(request, *args, **kwargs)
