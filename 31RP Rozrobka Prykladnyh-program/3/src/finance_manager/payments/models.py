from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    # links Account to each User
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # current account balance
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0) 
    # maximum credit allowed 
    credit_limit = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.user.username + '\'s Account'