from django.db import models

class Client(models.Model):
    name=models.CharField(max_length=127)
    balance=models.PositiveIntegerField(default=0)
    credit=models.PositiveIntegerField(default=0)
    manager=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name}{" (admin)" if self.manager else ""} has {self.balance} with {self.credit} limit'