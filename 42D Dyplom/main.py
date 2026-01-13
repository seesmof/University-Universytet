from nicegui import ui, app

money: int = 0
rate: int = 1
interval: float = 1.0


def add_money(rate: int):
    global money
    money = money + rate
    ui.update()
    timer.update()


timer = ui.timer(interval=interval, callback=lambda: add_money(rate=rate))

ui.label(f"{money = }")
ui.run(title="Agriculture Tycoon", favicon="🚜")
