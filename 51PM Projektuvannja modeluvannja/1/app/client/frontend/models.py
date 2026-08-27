from django.db import models


# Create your models here.
class Measurement(models.Model):
    value = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.value
