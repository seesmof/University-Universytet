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
    # Всі вантажівки
    trucks: list[ITruck] = list()
    # Всі кредити
    loans: list[ILoan] = list()
    # Всі замовлення
    orders: list[IOrder] = list()

    # Власні вантажівки
    owned_trucks: list[ITruck] = list()
    # Обрана вантажівка
    selected_truck: ITruck = None
    # Взяті кредити
    taken_loans: list[ILoan] = list()
    # Гроші користувача
    money: int = 0


class Const:
    CURRENT_FOLDER = os.path.dirname(os.path.abspath(__file__))


# --- ПОМІЧНИКИ ---


def convert_months_to_years(duration: int):
    MONTHS_IN_A_YEAR = 12

    years = duration // MONTHS_IN_A_YEAR
    months = duration % MONTHS_IN_A_YEAR

    return (
        # Повернути роки та місяці
        f"{years} років, {months} місяців"
        # Якщо надано обидва
        if months and years
        # Інакше == роки
        else f"{years} років"
        # Якщо їх надано
        if years
        # Інакше == місяці
        else f"{months} місяців"
    )


# --- ОНОВЛЕННЯ ---


def update_money():
    money_label.set_text(f"💸 {State.money}")
    money_label.update()


def update_selected_truck():
    selected_truck_label.set_text(
        # Встановити назву обраної вантажівки, якщо вона обрана. Інакше == нуль
        f"🚛 {State.selected_truck.name}" if State.selected_truck else ""
    )
    selected_truck_label.update()


# --- ЗАМОВЛЕННЯ ---


def perform_order(order: IOrder, map):
    # Якщо вантажівки не обрано
    if State.selected_truck is None:
        # Повідомити користувача про це
        ui.notify("Немає обраної вантажівки.", close_button="Добре")
        # Завершити роботу
        return

    # Додати до грошей користувача ціну замовлення
    State.money += order.price
    # Оновити лейбл
    update_money()

    # На мапі показати місто, куди йде замовлення
    map.set_center(order.coordinates)
    map.update()


# --- ВАНТАЖІВКИ ---


def select_truck(truck: ITruck):
    # Встановити обрану вантажівку у надану
    State.selected_truck = truck
    update_selected_truck()


def buy_truck(truck: ITruck):
    # Якщо користувацьких грошей менше за вартість вантажівки
    if State.money < truck.price:
        # Повідомити про це користувача
        ui.notify("Недостатньо коштів.", close_button="Добре")
        # Завершити роботу
        return

    # Відняти від грошей користувача ціну вантажівки
    State.money -= truck.price
    update_money()

    # До власних вантажівок додати куплену
    State.owned_trucks.append(truck)
    owned_trucks_view.refresh()

    # Встановити нову вантажівку як обрану
    select_truck(truck)
    # Повідомити користувача про успішну купівлю
    ui.notify(f"Куплено {truck.category.lower()} під назвою {truck.name}!")


def sell_truck(truck: ITruck):
    # Обнулити обрану вантажівку
    State.selected_truck = None
    update_selected_truck()

    # Прибрати вантажівку з придбаних
    State.owned_trucks.remove(truck)
    owned_trucks_view.refresh()
    # Повідомити користувача про успішний продаж
    ui.notify(f"Продано {truck.category.lower()} під назвою {truck.name}!")

    # Додати до грошей користувача ціну вантажівки
    State.money += truck.price
    update_money()


# --- КРЕДИТИ ---


def take_loan(loan: ILoan):
    # Додати до грошей користувача суму кредиту
    State.money += loan.amount
    # До взятих кредитів додати наданий
    State.taken_loans.append(loan)

    update_money()
    # Повідомити користувача про успішне взяття кредиту
    ui.notify(f"Взято кредит на ₴ {loan.amount} від {loan.bank}")
    loans_view.refresh()


def pay_loan(loan: ILoan):
    # Якщо грошей у користувача менше за суму кредиту
    if State.money < loan.amount:
        # Повідомити про це користувача
        ui.notify("Недостатньо коштів для сплати.", close_button="Добре")
        # Завершити роботу
        return

    # Від грошей користувача відняти суму кредиту
    State.money -= loan.amount
    # Від взятих кредитів прибрати наданий
    State.taken_loans.remove(loan)

    update_money()
    bank_view.refresh()
    loans_view.refresh()
    # Повідомити користувача про успішне сплачення кредиту
    ui.notify(f"Сплачено кредит на ₴ {loan.amount} від {loan.bank}")


# --- ПРЕДСТАВЛЕННЯ ІНТЕРФЕЙСУ ---


@ui.refreshable
def loans_view():
    # Якщо немає взятих кредитів
    if not State.taken_loans:
        # Повідомити про це користувача
        ui.label("Немає взятих кредитів.")
    with ui.grid(columns=2).classes("w-full"):
        # Для кожного взятого кредиту
        for loan in State.taken_loans:
            # Зробити картку
            with ui.card().tight():
                with ui.card_section():
                    # Назва кредиту
                    ui.label(f"Кредит у {loan.bank}").classes("font-medium")
                    # Триаалість кредиту
                    ui.label(f"на {convert_months_to_years(loan.duration)}")
                    with ui.row().classes("mt-4"):
                        # Сума кредиту
                        ui.label(f"₴ {loan.amount}")
                        # Сплатити кредит
                        ui.button(
                            "Сплатити",
                            on_click=lambda this_loan=loan: pay_loan(this_loan),
                        )


@ui.refreshable
def owned_trucks_view():
    if not State.owned_trucks:
        ui.label("Немає придбаних вантажівок.")
    with ui.grid(columns=3).classes("w-full"):
        # Для кожної вантажівки у придбаних
        for truck in State.owned_trucks:
            # Створити картку
            with ui.card().tight():
                # Обрахувати шлях до файлу картинки
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                # Вивести картинку
                ui.image(image_path)
                with ui.card_section():
                    # Назва вантажівки
                    ui.label(truck.name).classes("text-lg font-medium")
                    # Категорія вантажівки
                    ui.label(truck.category)
                    with ui.row().classes("flex flex-row gap-2 mt-4"):
                        # Обрати вантажівку
                        ui.button(
                            "Обрати",
                            on_click=lambda this_truck=truck: select_truck(this_truck),
                        )
                        # Продати вантажівку
                        ui.button(
                            "Продати",
                            on_click=lambda this_truck=truck: sell_truck(this_truck),
                        )


@ui.refreshable
def store_view():
    with ui.grid(columns=3).classes("w-full"):
        # Для кожної вантажівку у вантажівках
        for truck in State.trucks:
            # Створити картку
            with ui.card().tight():
                # Обрахувати шлях до файлу картинки
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                # Вивести картинку
                ui.image(image_path)
                with ui.card_section().classes("w-full"):
                    # Назва вантажівки
                    ui.label(truck.name).classes("text-lg font-medium")
                    # Категорія вантажівки
                    ui.label(truck.category)
                    with ui.row().classes("justify-between flex flex-row w-full mt-4"):
                        # Вартість вантажівки
                        ui.label(f"₴ {truck.price}").classes("font-bold ")
                        # Купити вантажівку
                        ui.button(
                            "Купити",
                            on_click=lambda this_truck=truck: buy_truck(this_truck),
                        )


@ui.refreshable
def bank_view():
    with ui.grid(columns=2).classes("w-full"):
        # Для кожного кредиту зі всіх кредитів
        for index, loan in enumerate(State.loans, start=1):
            # Створити картку
            with ui.card().tight():
                with ui.card_section():
                    # Назва кредиту
                    ui.label(f"Кредит у {loan.bank}").classes("font-medium text-lg")
                    # Тривалість кредиту
                    ui.label(convert_months_to_years(loan.duration))
                    with ui.row().classes("mt-4"):
                        # Вартість кредиту
                        ui.label(f"₴ {loan.amount}")
                        # Взяти кредит
                        ui.button(
                            "Взяти",
                            on_click=lambda this_loan=loan: take_loan(this_loan),
                        )


@ui.refreshable
def orders_view():
    with ui.row().classes("w-full"):
        # Зробити віджет мапи
        map = ui.leaflet(center=State.orders[0].coordinates, zoom=10)
    with ui.grid(columns=3).classes("w-full"):
        # Для кожного замовлення у всіх замовленнях
        for order in State.orders:
            # Зробити картку
            with ui.card():
                with ui.card_section().classes("w-full"):
                    # Пункт призначення замовлення
                    ui.label(order.location).classes("text-lg font-medium")
                    # Вартість замовлення
                    ui.label(f"₴ {order.price}").classes("mb-4")
                    # Виконати замовлення
                    ui.button(
                        "Виконати",
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
    ui.run(title="Магазин вантажівок", favicon="🚛")
