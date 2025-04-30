from django.contrib.auth.models import Group,User
from rest_framework import seralizers

class UserSerializer(seralizers.HyperlinkedModelSerializer):
    class Meta:
        model=User
        fields=['url','username','email','groups']

class GroupSerializer(seralizers.HyperlinkedModelSerializer):
    class Meta:
        model=Group
        fields=['url','name']

