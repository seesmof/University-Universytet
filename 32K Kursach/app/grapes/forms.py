from django.forms import ModelForm

from grapes.models import Bunch


class BunchForm(ModelForm):
    class Meta:
        model=Bunch
        fields="__all__"