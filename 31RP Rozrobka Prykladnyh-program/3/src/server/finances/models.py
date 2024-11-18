from django.db import models

# Create your models here.
class User(models.Model):
    limit=models.PositiveBigIntegerField(default=0,null=True,blank=True)
    balance=models.PositiveBigIntegerField(default=0)