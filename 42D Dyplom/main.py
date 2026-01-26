from dataclasses import dataclass
import os
from nicegui import ui


@dataclass
class Truck:
    name: str
    category: str
    price: int
    picture: str


class State:
    trucks: list[Truck] = list()
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


with ui.tabs().classes("w-full") as main_tabs:
    owned_tab = ui.tab(TabName.OWNED)
    store_tab = ui.tab(TabName.STORE)
    bank_tab = ui.tab(TabName.BANK)
with ui.tab_panels(tabs=main_tabs, value=store_tab).classes("w-full"):
    with ui.tab_panel(owned_tab):
        ui.label(TabName.OWNED)
    with ui.tab_panel(store_tab):
        for truck in State.trucks:
            with ui.card().tight():
                image_path: str = os.path.join(
                    Const.CURRENT_FOLDER, "images", f"{truck.picture}.jpg"
                )
                ui.image(image_path)
                with ui.card_section():
                    ui.label(truck.name).classes("text-lg font-medium")
                    ui.label(truck.category).classes("italic")
                    ui.label(truck.price).classes("font-bold")
    with ui.tab_panel(bank_tab):
        ui.label(TabName.BANK)


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


State.trucks = load_trucks()
ui.run()
ui.update()
