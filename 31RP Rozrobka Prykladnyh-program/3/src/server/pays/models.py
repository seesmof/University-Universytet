from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=100)
    balance = models.PositiveBigIntegerField(default=0)
    limit = models.PositiveBigIntegerField(default=0)
    manager = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}{" (admin)" if self.manager else ""}, has ₴{self.balance} with ₴{self.limit} limit'

class Pay(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    purpose = models.CharField(max_length=255)
    amount = models.PositiveBigIntegerField()
    periodic = models.BooleanField(default=False)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'₴{self.amount} by {self.user.name} for {self.purpose}'