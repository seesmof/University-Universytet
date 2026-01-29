import os
from narwhals import Duration
from peewee import *
import datetime

from main import BankName

db_name = "database.db"
db = SqliteDatabase(db_name)


class BaseModel(Model):
    class Meta:
        database = db


class Truck(BaseModel):
    name = CharField()
    category = CharField()
    price = IntegerField()
    picture = CharField()


class Loan(BaseModel):
    amount = IntegerField()
    duration = IntegerField()
    bank = CharField()


class Order(BaseModel):
    price = IntegerField()
    location = CharField()
    coordinates = CharField()


db.connect()
loans_data = [
    Loan(amount=1_000, duration=6, bank=BankName.CREDIT_AGRICOLE),
    Loan(amount=3_000, duration=12, bank=BankName.PRIVAT),
    Loan(amount=6_000, duration=24, bank=BankName.RAIFFEISEN),
    Loan(amount=8_000, duration=32, bank=BankName.UNIVERSAL),
    Loan(amount=12_000, duration=64, bank=BankName.UKR_GAS_BANK),
    Loan(amount=24_000, duration=128, bank=BankName.PRIVAT),
]
for loan in loans_data:
    l = Loan.create(amount=loan.amount, duration=loan.duration, bank=loan.bank)
    print(l.amount)
