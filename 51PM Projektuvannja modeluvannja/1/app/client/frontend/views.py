from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .forms import MeasurementForm
from .models import Measurement


# Create your views here.
def measurements_list(req: HttpRequest):
    measurements = Measurement.objects.all()
    context = {"measurements": measurements}
    return render(req, "measurements/list.html", context)


def create_measurement(req: HttpRequest):
    if req.method == "POST":
        form = MeasurementForm(req.POST)
        if form.is_valid():
            return HttpResponse("Form success.")
    else:
        form = MeasurementForm()

    return render(req, "measurements/create.html", {"form": form})
