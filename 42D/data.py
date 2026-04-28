from dataclasses import dataclass
from peewee import SqliteDatabase, Model, CharField, IntegerField


class TabName:
    LOANS = "Кредити"
    OWNED = "Гараж"
    STORE = "Автосалон"
    BANK = "Банк"
    ORDERS = "Замовлення"


class TruckCategory:
    LOCAL = "Бус"
    LORRY = "Вантажівка"
    OFFROAD = "Всюдихід"


class BankName:
    PRIVAT = "Приват Банк"
    RAIFFEISEN = "Райфайзен Банк"
    CREDIT_AGRICOLE = "Кредит Агріколь"
    UNIVERSAL = "Банк Універсал"
    UKR_GAS_BANK = "Укргазбанк"


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


def load_trucks() -> list[ITruck]:
    trucks: list[ITruck] = list()

    try:
        all_trucks_query = Truck.select()
    except Exception:
        print("ERROR: Failed to fetch the database.")
        return
    for row in all_trucks_query:
        truck = ITruck(
            name=row.name, category=row.category, price=row.price, picture=row.picture
        )
        trucks.append(truck)

    return trucks


def load_loans() -> list[ILoan]:
    loans: list[ILoan] = list()

    try:
        all_loans_query = Loan.select()
    except Exception:
        print("ERROR: Failed to fetch the database.")
        return
    for row in all_loans_query:
        loan = ILoan(amount=row.amount, duration=row.duration, bank=row.bank)
        loans.append(loan)

    return loans


def load_orders() -> list[IOrder]:
    orders: list[IOrder] = list()

    try:
        all_orders_query = Order.select()
    except Exception:
        print("ERROR: Failed to fetch the database.")
        return
    for row in all_orders_query:
        order = IOrder(
            price=row.price,
            location=row.location,
            coordinates=tuple(
                float(coordinate) for coordinate in row.coordinates.split(",")
            ),
        )
        orders.append(order)

    return orders
