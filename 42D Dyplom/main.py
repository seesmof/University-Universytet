from nicegui import ui
import os

from data import (
    ILoan,
    IOrder,
    TabName,
    ITruck,
    load_loans,
    load_orders,
    load_trucks,
)


class State:
    trucks: list[ITruck] = list()
    loans: list[ILoan] = list()
    orders: list[IOrder] = list()

    owned_trucks: list[ITruck] = list()
    selected_truck: ITruck = None
    taken_loans: list[ILoan] = list()
    money: int = 0


class Const:
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


# --- HELPER ---


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


# --- UPDATES ---


def update_money():
    money_label.set_text(f"💸 {State.money}")
    money_label.update()


def update_selected_truck():
    selected_truck_label.set_text(
        f"🚛 {State.selected_truck.name}" if State.selected_truck else ""
    )
    selected_truck_label.update()


# --- ORDERS ---


def perform_order(order: IOrder, map):
    if State.selected_truck is None:
        ui.notify("No selected truck", close_button="Sad")
        return

    State.money += order.price
    update_money()

    map.set_center(order.coordinates)
    map.update()


# --- TRUCKS ---


def select_truck(truck: ITruck):
    State.selected_truck = truck
    update_selected_truck()


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


# --- LOANS ---


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


# --- UI VIEWS ---


@ui.refreshable
def loans_view():
    if not State.taken_loans:
        ui.label("No loans taken yet.")
    with ui.grid(columns=2).classes("w-full"):
        for loan in State.taken_loans:
            with ui.card().tight():
                with ui.card_section():
                    ui.label(f"Loan @ {loan.bank}").classes("font-medium")
                    ui.label(convert_months_to_years(loan.duration))
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
    with ui.grid(columns=2).classes("w-full"):
        for index, loan in enumerate(State.loans, start=1):
            with ui.card().tight():
                with ui.card_section():
                    ui.label(f"Loan @ {loan.bank}").classes("font-medium text-lg")
                    ui.label(convert_months_to_years(loan.duration))
                    with ui.row().classes("mt-4"):
                        ui.label(f"$ {loan.amount}")
                        ui.button(
                            "Take",
                            on_click=lambda this_loan=loan: take_loan(this_loan),
                        )


@ui.refreshable
def orders_view():
    with ui.row().classes("w-full"):
        map = ui.leaflet(center=State.orders[0].coordinates, zoom=10)
    with ui.grid(columns=3).classes("w-full"):
        for order in State.orders:
            with ui.card():
                with ui.card_section():
                    ui.label(order.location).classes("text-lg font-medium")
                    ui.label(f"$ {order.price}").classes("mb-4")
                    ui.button(
                        "Perform",
                        on_click=lambda this_order=order: perform_order(
                            this_order, map
                        ),
                    )


State.trucks = load_trucks()
State.loans = load_loans()
State.orders = load_orders()

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
