from django.forms.models import ModelForm

from .models import Measurement


class MeasurementForm(ModelForm):
    class Meta:
        model = Measurement
        fields = ["value", "description"]
