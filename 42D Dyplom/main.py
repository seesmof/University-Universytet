from nicegui import ui

from soil import SOIL_COLOR, SoilWearType

soil_wear = {
    "0_0": SoilWearType.BEST,
    "0_1": SoilWearType.BEST,
    "0_2": SoilWearType.BEST,
    "1_0": SoilWearType.BEST,
    "1_1": SoilWearType.BEST,
    "1_2": SoilWearType.BEST,
    "2_0": SoilWearType.BEST,
    "2_1": SoilWearType.BEST,
    "2_2": SoilWearType.BEST,
}


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
            ui.button(color=SOIL_COLOR[soil_wear["0_0"]]).classes("aspect-square w-40")
            ui.button(color=SOIL_COLOR[soil_wear["0_1"]]).classes("aspect-square")
            ui.button(color=SOIL_COLOR[soil_wear["0_2"]]).classes("aspect-square")

            ui.button(color=SOIL_COLOR[soil_wear["1_0"]]).classes("aspect-square")
            ui.button(color=SOIL_COLOR[soil_wear["1_1"]]).classes("aspect-square")
            ui.button(color=SOIL_COLOR[soil_wear["1_2"]]).classes("aspect-square")

            ui.button(color=SOIL_COLOR[soil_wear["2_0"]]).classes("aspect-square")
            ui.button(color=SOIL_COLOR[soil_wear["2_1"]]).classes("aspect-square")
            ui.button(color=SOIL_COLOR[soil_wear["2_2"]]).classes("aspect-square")
    with ui.tab_panel(store_tab):
        ui.label(store_tab_name)

ui.run(title="Agriculture Tycoon", favicon="🚜")
