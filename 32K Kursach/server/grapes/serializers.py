from rest_framework import serializers

from grapes.models import Bunch

class BunchSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bunch
        fields="__all__"