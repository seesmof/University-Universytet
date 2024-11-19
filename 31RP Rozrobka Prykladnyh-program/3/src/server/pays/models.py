from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.PositiveBigIntegerField(default=0)
    limit = models.PositiveBigIntegerField(default=0)
    manager = models.BooleanField(default=False)

class Payment(models.Model):
    pass

class PeriodicPayment(models.Model):
    PAYMENT_PERIOD=[
        ('DAY','Day'),
        ('MONTH','Month'),
        ('YEAR','Year')
    ]
    period = models.CharField(choices=PAYMENT_PERIOD,default='DAY')
    next_date = models.DateField()