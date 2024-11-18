from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.PositiveBigIntegerField(default=0)
    limit = models.PositiveBigIntegerField(default=0)
    manager = models.BooleanField(default=False)

class Pay(models.Model):
    purpose = models.CharField(max_length=255)
    amount = models.PositiveBigIntegerField()
    periodic = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)