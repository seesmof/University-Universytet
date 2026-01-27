from dataclasses import dataclass
import os
from nicegui import ui


@dataclass
class Truck:
    name: str
    category: str
    price: int
    picture: str


@dataclass
class Loan:
    amount: int
    duration: int = 12


@dataclass
class Order:
    price: int
    location: str
    coordinates: tuple[float, float]


class State:
    trucks: list[Truck] = list()
    owned_trucks: list[Truck] = list()
    money: int = 0


class Const:
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))
    VIEW_CONTAINER_CLASSES = "w-full"


class TabName:
    OWNED = "Owned"
    STORE = "Store"
    BANK = "Bank"
    ORDERS = "Orders"


class TruckCategory:
    LOCAL = "Local"
    LORRY = "Lorry"
    OFFORAD = "Offroad"


def load_trucks() -> list[Truck]:
    file_name: str = "trucks.csv"
    file_path: str = os.path.join(Const.CURRENT_FOLDER, file_name)

    with open(file_path, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
    lines = [
        Truck(*line.strip().split(","))
        for index, line in enumerate(lines)
        if index != 0
    ]
    for truck in lines:
        truck.price = int(truck.price)

    return lines


def convert_months_to_years(duration: int):
    MONTHS_IN_A_YEAR = 12

    years = duration // MONTHS_IN_A_YEAR
    months = duration % MONTHS_IN_A_YEAR

    return f"{years} years, {months} months" if months else f"{years} years"


def take_loan(amount: int):
    State.money += amount
    update_money()


def buy_truck(truck: Truck):
    if State.money < truck.price:
        ui.notify("Not enough money", close_button="Sad")
        return

    State.money -= truck.price
    State.owned_trucks.append(truck)

    update_money()
    owned_trucks_view.refresh()
    ui.notify(f"Bought {truck.name}!")


def update_money():
    money_label.set_text(f"💸 {State.money}")
    money_label.update()


def sell_truck(truck: Truck):
    found_truck: Truck = [t for t in State.owned_trucks if t.name == truck.name][0]
    State.owned_trucks.remove(found_truck)
    owned_trucks_view.refresh()
    ui.notify(f"Sold {truck.name}!")

    State.money += truck.price
    update_money()


@ui.refreshable
def owned_trucks_view():
    with ui.grid(columns=3).classes(Const.VIEW_CONTAINER_CLASSES):
        for truck in State.owned_trucks:
            with ui.card().tight():
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                ui.image(image_path)
                with ui.card_section():
                    ui.label(truck.name).classes("text-lg font-medium")
                    ui.label(truck.category).classes("italic py-2")
                    ui.button("Sell", on_click=lambda t=truck: sell_truck(t))


@ui.refreshable
def store_view():
    with ui.grid(columns=3).classes(Const.VIEW_CONTAINER_CLASSES):
        for truck in State.trucks:
            with ui.card().tight():
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                ui.image(image_path)
                with ui.card_section().classes("w-full"):
                    ui.label(truck.name).classes("text-lg font-medium")
                    ui.label(truck.category).classes("italic")
                    with ui.row().classes("justify-between flex flex-row w-full mt-2"):
                        ui.label(f"$ {truck.price}").classes("font-bold ")
                        ui.button("Buy", on_click=lambda t=truck: buy_truck(t))


@ui.refreshable
def bank_view():
    loans_data = [
        Loan(amount=3_000, duration=12),
        Loan(amount=6_000, duration=24),
        Loan(amount=8_000, duration=32),
        Loan(amount=12_000, duration=64),
        Loan(amount=24_000, duration=128),
    ]

    with ui.grid(columns=3).classes(Const.VIEW_CONTAINER_CLASSES):
        for index, loan in enumerate(loans_data, start=1):
            with ui.card().tight():
                with ui.card_section():
                    ui.label(f"Loan #{index}").classes("font-medium text-lg")
                    ui.label(convert_months_to_years(loan.duration))
                    with ui.row().classes("mt-2"):
                        ui.label(f"$ {loan.amount}")
                        ui.button("Take", on_click=lambda l=loan: take_loan(l.amount))


@ui.refreshable
def orders_view():
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
            location="Kharkiv, Ukraine",
            coordinates=(50.00195062385631, 36.29946397006903),
        ),
        Order(
            price=6_000,
            location="Zhytomyr, Ukraine",
            coordinates=(50.272590573692035, 28.70071890452024),
        ),
    ]

    with ui.row().classes(Const.VIEW_CONTAINER_CLASSES):
        map = ui.leaflet(center=orders_data[0].coordinates, zoom=10)
    with ui.grid(columns=3).classes(Const.VIEW_CONTAINER_CLASSES):
        for order in orders_data:
            with ui.card():
                with ui.card_section():
                    ui.label(order.location).classes("text-lg font-medium")
                    ui.label(f"$ {order.price}").classes("italic py-4")
                    ui.button("Get", on_click=lambda o=order: perform_order(o, map))


def perform_order(order: Order, map):
    State.money += order.price
    update_money()

    map.set_center(order.coordinates)
    map.update()


State.trucks = load_trucks()

money_label = ui.label(f"💸 {State.money}").classes("self-end")
with ui.tabs().classes("w-full") as main_tabs:
    owned_tab = ui.tab(TabName.OWNED)
    store_tab = ui.tab(TabName.STORE)
    orders_tab = ui.tab(TabName.ORDERS)
    bank_tab = ui.tab(TabName.BANK)

with ui.tab_panels(tabs=main_tabs, value=store_tab).classes("w-full"):
    with ui.tab_panel(owned_tab):
        owned_trucks_view()
    with ui.tab_panel(store_tab):
        store_view()
    with ui.tab_panel(orders_tab):
        orders_view()
    with ui.tab_panel(bank_tab):
        bank_view()

ui.run(title="Trucks Store", favicon="🚛")
