import os
from peewee import *
import datetime

from data import IOrder
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
all_orders_query = Order.select()
for row in all_orders_query:
    order = IOrder(
        price=row.price, location=row.location, coordinates=row.coordinates.split(",")
    )
    print(order)
