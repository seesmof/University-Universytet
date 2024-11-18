from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    balance = models.PositiveBigIntegerField(default=0)
    credit_limit = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.username

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.PositiveBigIntegerField()
    date = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.description} by {self.user.username} for {self.amount} on {self.date}"