from django.shortcuts import render

from .models import Measurement


# Create your views here.
def measurements_list(req):
    measurements = Measurement.objects.all()

    context = {"measurements": measurements}
    return render(req, "measurements/list.html", context)
