from nicegui import ui

with ui.tabs().classes("w-full") as main_page_tabs:
    tools_tab_name = "Tools"
    field_tab_name = "Field"
    store_tab_name = "Store"
    tools_tab = ui.tab(tools_tab_name, icon="build")
    field_tab = ui.tab(field_tab_name, icon="grass")
    store_tab = ui.tab(store_tab_name, icon="local_grocery_store")

with ui.tab_panels(tabs=main_page_tabs, value=tools_tab_name):
    with ui.tab_panel(tools_tab):
        ui.label(tools_tab_name)
    with ui.tab_panel(field_tab):
        ui.label(field_tab_name)
    with ui.tab_panel(store_tab):
        ui.label(store_tab_name)


ui.run(title="Agriculture Tycoon", favicon="🚜")
