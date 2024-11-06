from django.db import models

class User(models.Model):
    name:str['username']
    password:str['password']
    balance:int['money']
    limit:int['money']
    kind:str['client'|'manager']

class Payment(models.Model):
    amount:int['money']
    user:str['User.id']
    kind:str['single'|'periodic']
    next_payout:str['date']