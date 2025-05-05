from django.db import models

# Create your models here.
class Bunch(models.Model):
    count=models.IntegerField(default=0)
    outside=models.BooleanField(default=False)
    shape=models.BooleanField(default=False)
    color=models.BooleanField(default=False)
    sugar=models.BooleanField(default=False)

    class Stage(models.TextChoices):
        Juice='Juice'
        Wine='Wine'
        Grapes='Grapes'
        Raisins='Raisins'
        Jelly='Jelly'
    stage=models.CharField(max_length=7,choices=Stage,blank=True)

    def __str__(self):
        return f'{self.count} grapes: outside {self.outside}, shape {self.shape}, color {self.color}, sugar {self.sugar}. Stage: {self.stage}'
