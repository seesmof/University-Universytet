from django.db import models

# Create your models here.
class Bunch(models.Model):
    count=models.IntegerField(blank=False)
    outside=models.BooleanField(blank=False)
    sugar=models.BooleanField(blank=False)
    shape=models.BooleanField(blank=False)
    color=models.BooleanField(blank=False)
    color=models.BooleanField()

    def __str__(self):
        return f'{self.count} grapes: outside {"damaged" if self.outside else "okay"}, sugar {"imbalanced" if self.sugar else "okay"}, shape {"uneven" if self.shape else "okay"}, color {"changed" if self.color else "okay"}'
    