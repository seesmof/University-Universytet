from django.db import models

class User(models.Model):
    name=models.CharField(max_length=217)
    password=models.CharField(max_length=127)
    balance=models.PositiveIntegerField()
    limit=models.PositiveIntegerField()
    class UserKind(models.TextChoices):
        CLIENT='C'
        MANAGER='M'
    kind=models.CharField(
        max_length=1,
        choices=UserKind,
        default=UserKind.CLIENT
    )

    def __str__(self) -> str:
        return f'{self.name} has ₴{self.balance} limited to ₴{self.limit} and is a {"client" if self.kind=="C" else "manager"}'

class Payment(models.Model):
    amount=models.PositiveIntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    class PaymentKind(models.TextChoices):
        SINGLE='S'
        PERIODIC='P'
    kind=models.CharField(
        max_length=1,
        choices=PaymentKind,
        default=PaymentKind.SINGLE
    )
    date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{"single" if self.kind=="S" else "periodic"} for ₴{self.amount} by {self.user.name}, next for {self.date}'