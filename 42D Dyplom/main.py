from collections import namedtuple
from nicegui import ui

from soil import SOIL_COLOR, SoilWearType

Soil = namedtuple("Soil", "wear,times_used")

soil_state = {
    "0_0": Soil(wear=SoilWearType.BEST, times_used=0),
    "0_1": Soil(wear=SoilWearType.BEST, times_used=0),
    "0_2": Soil(wear=SoilWearType.BEST, times_used=0),
    "1_0": Soil(wear=SoilWearType.BEST, times_used=0),
    "1_1": Soil(wear=SoilWearType.BEST, times_used=0),
    "1_2": Soil(wear=SoilWearType.BEST, times_used=0),
    "2_0": Soil(wear=SoilWearType.BEST, times_used=0),
    "2_1": Soil(wear=SoilWearType.BEST, times_used=0),
    "2_2": Soil(wear=SoilWearType.BEST, times_used=0),
}
money_state: int = 0
rate: int = 1


def use_soil(field_index: str):
    global money_state
    money_state += rate
    print(money_state)

    update_soil(field_index)
    money_label.update()


def update_soil(index: int):
    soil_sample = soil_state[index]
    print(soil_sample)


money_label = ui.label(text=f"💸 {money_state}").classes("self-end")

with ui.tabs().classes("w-full") as main_page_tabs:
    tools_tab_name = "Інструменти"
    field_tab_name = "Поле"
    store_tab_name = "Крамниця"
    tools_tab = ui.tab(tools_tab_name, icon="build")
    field_tab = ui.tab(field_tab_name, icon="grass")
    store_tab = ui.tab(store_tab_name, icon="local_grocery_store")

with ui.tab_panels(tabs=main_page_tabs, value=field_tab_name):
    with ui.tab_panel(tools_tab):
        ui.label(tools_tab_name)
    with ui.tab_panel(field_tab):
        with ui.grid(columns=3):
            ui.button(
                on_click=lambda: use_soil("0_0"),
                color=SOIL_COLOR[soil_state["0_0"].wear],
            ).classes("aspect-square w-40")
            ui.button(
                on_click=lambda: use_soil("0_1"),
                color=SOIL_COLOR[soil_state["0_1"].wear],
            ).classes("aspect-square")
            ui.button(
                on_click=lambda: use_soil("0_2"),
                color=SOIL_COLOR[soil_state["0_2"].wear],
            ).classes("aspect-square")

            ui.button(
                on_click=lambda: use_soil("1_0"),
                color=SOIL_COLOR[soil_state["1_0"].wear],
            ).classes("aspect-square")
            ui.button(
                on_click=lambda: use_soil("1_1"),
                color=SOIL_COLOR[soil_state["1_1"].wear],
            ).classes("aspect-square")
            ui.button(
                on_click=lambda: use_soil("1_2"),
                color=SOIL_COLOR[soil_state["1_2"].wear],
            ).classes("aspect-square")

            ui.button(
                on_click=lambda: use_soil("2_0"),
                color=SOIL_COLOR[soil_state["2_0"].wear],
            ).classes("aspect-square")
            ui.button(
                on_click=lambda: use_soil("2_1"),
                color=SOIL_COLOR[soil_state["2_1"].wear],
            ).classes("aspect-square")
            ui.button(
                on_click=lambda: use_soil("2_2"),
                color=SOIL_COLOR[soil_state["2_2"].wear],
            ).classes("aspect-square")
    with ui.tab_panel(store_tab):
        ui.label(store_tab_name)

ui.run(title="Agriculture Game", favicon="🚜")
