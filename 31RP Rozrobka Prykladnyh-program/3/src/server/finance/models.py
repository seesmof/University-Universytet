from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=127)
    balance=models.PositiveIntegerField(default=0)
    credit=models.PositiveIntegerField(default=0)
    manager=models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
class Payment(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    timestamp=models.DateTimeField()
    purpose=models.TextField()
    amount=models.PositiveIntegerField()

    def __str__(self):
        return f'{self.purpose} on {self.timestamp} by {self.client.name} for {self.amount}'