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
    amount=models.PositiveIntegerField()
    purpose=models.TextField()
    OPERATIONS=[
        ('WIT','Withdrawal'),
        ('DEP','Deposit'),
    ]
    operation=models.CharField(max_length=3,choices=OPERATIONS)
    KINDS=[
        ('SNG','Single'),
        ('PER','Periodic'),
    ]
    kind=models.CharField(max_length=3,choices=KINDS)

    def __str__(self):
        return f'{self.purpose} on {self.timestamp.strftime('%d.%m.%Y at %H:%M:%S')} by {self.client.name} for {self.amount}'

# add PeriodicPayment class, in client page add 'Pay' button, on click update next_date based on period taken from (DAY, MONTH, YEAR)