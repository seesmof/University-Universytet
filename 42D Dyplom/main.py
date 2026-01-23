from nicegui import ui

with ui.tabs().classes("w-full") as main_tabs:
    one = ui.tab("One")
    two = ui.tab("Two")
with ui.tab_panels(main_tabs, value=two).classes("w-full"):
    with ui.tab_panel(one):
        ui.label("First tab")
    with ui.tab_panel(two):
        ui.label("Second tab")

ui.run()
