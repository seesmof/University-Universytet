from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    balance = models.PositiveBigIntegerField(default=0)
    limit = models.PositiveBigIntegerField(default=0)
    is_manager = models.BooleanField(default=False)

""" 
class Payment(models.Model):
    pass

class PeriodicPayment(models.Model):
    PAYMENT_PERIODS=[
        ('DAY','Day'),
        ('MONTH','Month'),
        ('YEAR','Year')
    ]
    period = models.CharField(choices=PAYMENT_PERIODS,default='DAY',max_length=5)
    next_date = models.DateField()

class Entry(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField()
    amount = models.PositiveIntegerField()
    purpose = models.TextField()
"""