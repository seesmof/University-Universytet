from nicegui import ui

with ui.card().classes("mx-auto"):
    ui.label(
        "Так бо Бог полюбив світ, що дав Сина Свого Однородженого, щоб кожен, хто вірує в Нього, не згинув, але мав життя вічне. (Йоан 3:16)"
    )


class TabNames:
    BINARY = "Binary"
    MONTGOMERY = "Montgomery"
    RIDGE = "Ridge"


with ui.tabs().classes("w-full") as main_tabs:
    binary = ui.tab(TabNames.BINARY)
    montgomery = ui.tab(TabNames.MONTGOMERY)
    ridge = ui.tab(TabNames.RIDGE)
with ui.tab_panels(main_tabs, value=TabNames.BINARY).classes("w-full"):
    with ui.tab_panel(TabNames.BINARY):
        ui.label("Binary")
    with ui.tab_panel(TabNames.MONTGOMERY):
        ui.label("Montgomery")
    with ui.tab_panel(TabNames.RIDGE):
        ui.label("Ridge")

ui.run(title="TR2", favicon="🔬")
