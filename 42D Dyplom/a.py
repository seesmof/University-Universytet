import os
from narwhals import Duration
from peewee import *
import datetime

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
db.create_tables([Order, Truck, Loan])

file_name: str = "trucks.csv"
file_path: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), file_name)
with open(file_path, encoding="utf-8", mode="r") as f:
    lines = f.readlines()
for line in lines:
    data = line.strip().split(",")
    truck = Truck.create(name=data[0], category=data[1], price=data[2], picture=data[3])
    print(truck.name)
