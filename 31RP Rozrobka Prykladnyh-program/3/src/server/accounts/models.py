from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    balance=models.PositiveIntegerField(default=0)
    limit=models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.username} has {self.balance} with limit of {self.limit}'