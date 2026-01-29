from dataclasses import dataclass
from peewee import *


class TabName:
    LOANS = "Loans"
    OWNED = "Trucks"
    STORE = "Store"
    BANK = "Bank"
    ORDERS = "Orders"


class TruckCategory:
    LOCAL = "Local"
    LORRY = "Lorry"
    OFFORAD = "Offroad"


class BankName:
    PRIVAT = "Privat Bank"
    RAIFFEISEN = "Raiffeisen Bank"
    CREDIT_AGRICOLE = "Crédit Agricole"
    UNIVERSAL = "Universal Bank"
    UKR_GAS_BANK = "Ukrgasbank"


@dataclass
class ITruck:
    name: str
    category: TruckCategory
    price: int
    picture: str


@dataclass
class ILoan:
    amount: int
    duration: int
    bank: BankName


@dataclass
class IOrder:
    price: int
    location: str
    coordinates: tuple[float, float]


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


def load_orders() -> list[IOrder]:
    orders: list[IOrder] = list()

    all_orders_query = Order.select()
    for row in all_orders_query:
        order = IOrder(
            price=row.price,
            location=row.location,
            coordinates=row.coordinates.split(","),
        )
        orders.append(order)

    return orders


def load_loans() -> list[ILoan]:
    loans: list[ILoan] = list()

    all_loans_query = Loan.select()
    for row in all_loans_query:
        loan = ILoan(amount=row.amount, duration=row.duration, bank=row.bank)
        loans.append(loan)

    return loans


def load_trucks() -> list[ITruck]:
    trucks: list[ITruck] = list()

    all_trucks_query = Truck.select()
    for row in all_trucks_query:
        truck = ITruck(
            name=row.name, category=row.category, price=row.price, picture=row.picture
        )
        trucks.append(truck)

    return trucks
