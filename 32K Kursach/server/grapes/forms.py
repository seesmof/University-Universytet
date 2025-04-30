from django.forms import ModelForm

from grapes.models import Bunch


class BunchForm(ModelForm):
    class Meta:
        model=Bunch
        fields=('count','outside','sugar','shape','color')