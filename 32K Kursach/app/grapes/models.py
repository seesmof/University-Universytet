from django.db import models

# Create your models here.
class Bunch(models.Model):
    count=models.IntegerField(blank=False)
    outside=models.BooleanField(blank=False)
    sugar=models.BooleanField(blank=False)
    shape=models.BooleanField(blank=False)
    color=models.BooleanField(blank=False)