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
        ('Withdrawal','Withdrawal'),
        ('Deposit','Deposit'),
    ]
    operation=models.CharField(max_length=12,choices=OPERATIONS)
    KINDS=[
        ('Single','Single'),
        ('Periodic','Periodic'),
    ]
    kind=models.CharField(max_length=12,choices=KINDS)

    def __str__(self):
        return f'{self.purpose} on {self.timestamp.strftime('%d.%m.%Y at %H:%M:%S')} by {self.client.name} for {self.amount}'
    
# add PeriodicPayment class, in client page add 'Pay' button, on click update next_date based on period taken from (DAY, MONTH, YEAR). in client page also add 'New Periodic Payment' button to create one
class PeriodicPayment(models.Model):
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    amount=models.PositiveIntegerField()
    purpose=models.TextField()
    PERIODS=[
        ('Day','Day'),
        ('Month','Month'),
        ('Year','Year'),
    ]
    period=models.CharField(max_length=12,choices=PERIODS)
    next_date=models.DateField()