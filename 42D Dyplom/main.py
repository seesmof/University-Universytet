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


class State:
    trucks: list[Truck] = list()
    owned_trucks: list[Truck] = list()
    money: int = 0


class Const:
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


class TabName:
    OWNED = "Owned"
    STORE = "Store"
    BANK = "Bank"


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
    return lines


def convert_months_to_years(duration: int):
    MONTHS_IN_A_YEAR = 12

    years = duration // MONTHS_IN_A_YEAR
    months = duration % MONTHS_IN_A_YEAR

    return f"{years} years, {months} months" if months else f"{years} years"


def take_loan(amount: int):
    print(f"Taking loan for {amount}")
    State.money += amount
    money_label.text = f"💸 {State.money}"
    money_label.update()


State.trucks = load_trucks()
loans_data = [
    Loan(amount=3_000, duration=12),
    Loan(amount=6_000, duration=24),
    Loan(amount=8_000, duration=32),
    Loan(amount=12_000, duration=64),
    Loan(amount=24_000, duration=128),
]

money_label = ui.label(f"💸 {State.money}").classes("self-end")
with ui.tabs().classes("w-full") as main_tabs:
    owned_tab = ui.tab(TabName.OWNED)
    store_tab = ui.tab(TabName.STORE)
    bank_tab = ui.tab(TabName.BANK)
with ui.tab_panels(tabs=main_tabs, value=store_tab).classes("w-full"):
    with ui.tab_panel(owned_tab):
        with ui.grid(columns=3):
            for truck in State.owned_trucks:
                with ui.card().tight():
                    image_path: str = os.path.join(
                        Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                    )
                    ui.image(image_path)
                    with ui.card_section():
                        ui.label(truck.name).classes("text-lg font-medium")
                        ui.label(truck.category).classes("italic")

    with ui.tab_panel(store_tab):
        with ui.grid(columns=3):
            for truck in State.trucks:
                with ui.card().tight():
                    image_path: str = os.path.join(
                        Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                    )
                    ui.image(image_path)
                    with ui.card_section():
                        ui.label(truck.name).classes("text-lg font-medium")
                        ui.label(truck.category).classes("italic")
                        with ui.row().classes(
                            "justify-between flex flex-row w-full mt-2"
                        ):
                            ui.label(f"$ {truck.price}").classes("font-bold ")
                            ui.button("Buy").props("outline")

    with ui.tab_panel(bank_tab):
        with ui.grid(columns=3):
            for index, loan in enumerate(loans_data, start=1):
                with ui.card().tight():
                    with ui.card_section():
                        ui.label(f"Loan #{index}").classes("font-medium text-lg")
                        ui.label(convert_months_to_years(loan.duration))
                        with ui.row().classes("mt-2"):
                            ui.label(f"$ {loan.amount}")
                            ui.button("Take", on_click=lambda: take_loan(loan.amount))


ui.run()
