from dataclasses import dataclass
from nicegui import ui
import os

from data import BankName, ILoan, IOrder, TabName, ITruck


class State:
    trucks: list[ITruck] = list()
    owned_trucks: list[ITruck] = list()
    selected_truck: ITruck = None
    taken_loans: list[ILoan] = list()
    money: int = 0


class Const:
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


def load_trucks() -> list[ITruck]:
    file_name: str = "trucks.csv"
    file_path: str = os.path.join(Const.CURRENT_FOLDER, file_name)

    with open(file_path, encoding="utf-8", mode="r") as f:
        lines = f.readlines()
    lines = [
        ITruck(*line.strip().split(","))
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

    return (
        f"{years} years, {months} months"
        if months and years
        else f"{years} years"
        if years
        else f"{months} months"
    )


def update_money():
    money_label.set_text(f"💸 {State.money}")
    money_label.update()


def update_selected_truck():
    selected_truck_label.set_text(
        f"🚛 {State.selected_truck.name}" if State.selected_truck else ""
    )
    selected_truck_label.update()


def perform_order(order: IOrder, map):
    if State.selected_truck is None:
        ui.notify("No selected truck", close_button="Sad")
        return

    State.money += order.price
    update_money()

    map.set_center(order.coordinates)
    map.update()


def buy_truck(truck: ITruck):
    if State.money < truck.price:
        ui.notify("Not enough money", close_button="Sad")
        return

    State.money -= truck.price
    update_money()

    State.owned_trucks.append(truck)
    owned_trucks_view.refresh()

    select_truck(truck)
    ui.notify(f"Bought {truck.name}!")


def sell_truck(truck: ITruck):
    State.selected_truck = None
    update_selected_truck()

    State.owned_trucks.remove(truck)
    owned_trucks_view.refresh()
    ui.notify(f"Sold {truck.name}!")

    State.money += truck.price
    update_money()


def select_truck(truck: ITruck):
    State.selected_truck = truck
    update_selected_truck()


def take_loan(loan: ILoan):
    State.money += loan.amount
    State.taken_loans.append(loan)

    update_money()
    ui.notify(f"Taken a loan for {loan.amount} from {loan.bank}")
    loans_view.refresh()


def pay_loan(loan: ILoan):
    if State.money < loan.amount:
        ui.notify("Not enough money to pay.", close_button="Sad")
        return

    State.money -= loan.amount
    State.taken_loans.remove(loan)

    update_money()
    bank_view.refresh()
    loans_view.refresh()
    ui.notify(f"Payed a loan for {loan.amount} from {loan.bank}")


@ui.refreshable
def loans_view():
    if not State.taken_loans:
        ui.label("No loans taken yet.")
    with ui.grid(columns=2).classes("w-full"):
        for loan in State.taken_loans:
            with ui.card().tight():
                with ui.card_section():
                    ui.label(f"Loan @ {loan.bank}").classes("font-medium")
                    ui.label(f"Duration: {loan.duration}")
                    with ui.row().classes("mt-4"):
                        ui.label(f"$ {loan.amount}")
                        ui.button(
                            "Pay", on_click=lambda this_loan=loan: pay_loan(this_loan)
                        )


@ui.refreshable
def owned_trucks_view():
    if not State.owned_trucks:
        ui.label("No trucks bought yet.")
    with ui.grid(columns=3).classes("w-full"):
        for truck in State.owned_trucks:
            with ui.card().tight():
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                ui.image(image_path)
                with ui.card_section():
                    ui.label(truck.name).classes("text-lg font-medium")
                    ui.label(truck.category)
                    with ui.row().classes("flex flex-row gap-2 mt-4"):
                        ui.button(
                            "Select",
                            on_click=lambda this_truck=truck: select_truck(this_truck),
                        )
                        ui.button(
                            "Sell",
                            on_click=lambda this_truck=truck: sell_truck(this_truck),
                        )


@ui.refreshable
def store_view():
    with ui.grid(columns=3).classes("w-full"):
        for truck in State.trucks:
            with ui.card().tight():
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                ui.image(image_path)
                with ui.card_section().classes("w-full"):
                    ui.label(truck.name).classes("text-lg font-medium")
                    ui.label(truck.category)
                    with ui.row().classes("justify-between flex flex-row w-full mt-4"):
                        ui.label(f"$ {truck.price}").classes("font-bold ")
                        ui.button(
                            "Buy",
                            on_click=lambda this_truck=truck: buy_truck(this_truck),
                        )


@ui.refreshable
def bank_view():
    loans_data = [
        ILoan(amount=1_000, duration=6, bank=BankName.CREDIT_AGRICOLE),
        ILoan(amount=3_000, duration=12, bank=BankName.PRIVAT),
        ILoan(amount=6_000, duration=24, bank=BankName.RAIFFEISEN),
        ILoan(amount=8_000, duration=32, bank=BankName.UNIVERSAL),
        ILoan(amount=12_000, duration=64, bank=BankName.UKR_GAS_BANK),
        ILoan(amount=24_000, duration=128, bank=BankName.PRIVAT),
    ]

    with ui.grid(columns=2).classes("w-full"):
        for index, loan in enumerate(loans_data, start=1):
            with ui.card().tight():
                with ui.card_section():
                    ui.label(f"Loan @ {loan.bank}").classes("font-medium text-lg")
                    ui.label(convert_months_to_years(loan.duration))
                    with ui.row().classes("mt-4 w-full"):
                        ui.label(f"$ {loan.amount}")
                        ui.button(
                            "Take",
                            on_click=lambda this_loan=loan: take_loan(this_loan),
                        )


@ui.refreshable
def orders_view():
    orders_data = [
        IOrder(
            price=3_000,
            location="Berlin",
            coordinates=(52.518744170403735, 13.406213091838993),
        ),
        IOrder(
            price=4_000,
            location="London",
            coordinates=(51.5067928552932, -0.12607730720849492),
        ),
        IOrder(
            price=6_000,
            location="Warsaw",
            coordinates=(52.23561758864598, 21.018099697575668),
        ),
        IOrder(
            price=7_000,
            location="Kyiv",
            coordinates=(50.458441369448394, 30.53985208331925),
        ),
        IOrder(
            price=3_000,
            location="Hannover",
            coordinates=(52.385944377042954, 9.727804834523267),
        ),
        IOrder(
            price=2_000,
            location="Hamburg",
            coordinates=(53.55052975065959, 9.992920102015772),
        ),
        IOrder(
            price=9_000,
            location="Lviv",
            coordinates=(49.841397119257735, 24.032740882395462),
        ),
        IOrder(
            price=4_000,
            location="Katowice",
            coordinates=(50.254720297302, 18.697951949786837),
        ),
        IOrder(
            price=6_000,
            location="Kharkiv",
            coordinates=(50.00195062385631, 36.29946397006903),
        ),
        IOrder(
            price=8_000,
            location="Zaporizhzhia",
            coordinates=(47.839790847405894, 35.13965215348557),
        ),
        IOrder(
            price=9_000,
            location="Prague",
            coordinates=(50.0733649767132, 14.434635200695334),
        ),
        IOrder(
            price=10_000,
            location="Paris",
            coordinates=["48.85755675929906", "2.352366598522737"],
        ),
    ]

    with ui.row().classes("w-full"):
        map = ui.leaflet(center=orders_data[0].coordinates, zoom=10)
    with ui.grid(columns=3).classes("w-full"):
        for order in orders_data:
            with ui.card():
                with ui.card_section():
                    ui.label(order.location).classes("text-lg font-medium")
                    ui.label(f"$ {order.price}").classes("italic py-4")
                    ui.button(
                        "Perform",
                        on_click=lambda this_order=order: perform_order(
                            this_order, map
                        ),
                    )


State.trucks = load_trucks()

with ui.row().classes("flex flex-row gap-4 self-end"):
    selected_truck_label = ui.label(
        f"🚛 {State.selected_truck.name}" if State.selected_truck else ""
    )
    money_label = ui.label(f"💸 {State.money}")
with ui.tabs().classes("w-full") as main_tabs:
    loans_tab = ui.tab(TabName.LOANS, icon="o_credit_score")
    owned_tab = ui.tab(TabName.OWNED, icon="o_warehouse")
    store_tab = ui.tab(TabName.STORE, icon="o_store")
    bank_tab = ui.tab(TabName.BANK, icon="o_account_balance")
    orders_tab = ui.tab(TabName.ORDERS, icon="o_list_alt")
with ui.tab_panels(tabs=main_tabs, value=store_tab).classes("w-full"):
    with ui.tab_panel(loans_tab):
        loans_view()
    with ui.tab_panel(owned_tab):
        owned_trucks_view()
    with ui.tab_panel(store_tab):
        store_view()
    with ui.tab_panel(bank_tab):
        bank_view()
    with ui.tab_panel(orders_tab):
        orders_view()

if __name__ in {"__main__", "__mp_main__"}:
    ui.run(title="Trucks Store", favicon="🚛")
