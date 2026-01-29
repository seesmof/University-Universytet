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
orders_data = [
    Order(
        price=3_000,
        location="Berlin",
        coordinates=(52.518744170403735, 13.406213091838993),
    ),
    Order(
        price=4_000,
        location="London",
        coordinates=(51.5067928552932, -0.12607730720849492),
    ),
    Order(
        price=6_000,
        location="Warsaw",
        coordinates=(52.23561758864598, 21.018099697575668),
    ),
    Order(
        price=7_000,
        location="Kyiv",
        coordinates=(50.458441369448394, 30.53985208331925),
    ),
    Order(
        price=3_000,
        location="Hannover",
        coordinates=(52.385944377042954, 9.727804834523267),
    ),
    Order(
        price=2_000,
        location="Hamburg",
        coordinates=(53.55052975065959, 9.992920102015772),
    ),
    Order(
        price=9_000,
        location="Lviv",
        coordinates=(49.841397119257735, 24.032740882395462),
    ),
    Order(
        price=4_000,
        location="Katowice",
        coordinates=(50.254720297302, 18.697951949786837),
    ),
    Order(
        price=6_000,
        location="Kharkiv",
        coordinates=(50.00195062385631, 36.29946397006903),
    ),
    Order(
        price=8_000,
        location="Zaporizhzhia",
        coordinates=(47.839790847405894, 35.13965215348557),
    ),
    Order(
        price=9_000,
        location="Prague",
        coordinates=(50.0733649767132, 14.434635200695334),
    ),
    Order(
        price=10_000,
        location="Paris",
        coordinates=(48.85755675929906, 2.352366598522737),
    ),
]
for order in orders_data:
    o = Order.create(
        price=order.price,
        location=order.location,
        coordinates=f"{order.coordinates[0]},{order.coordinates[1]}",
    )
    print(o.coordinates)
