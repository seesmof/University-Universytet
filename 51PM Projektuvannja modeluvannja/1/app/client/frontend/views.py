from django.http import HttpRequest
from django.shortcuts import render

from .models import Measurement


# Create your views here.
def measurements_list(req: HttpRequest):
    measurements = Measurement.objects.all()
    context = {"measurements": measurements}
    return render(req, "measurements/list.html", context)


def create_measurement(req: HttpRequest):
    if req.method == "POST":
        ...
