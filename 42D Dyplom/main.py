from nicegui import ui


money = 10

money_label = ui.label(f"Money: 💸 {money}")


def update_money():
    money_label.text = f"Money: 💸 20"
    money_label.update()


ui.button("Update", on_click=update_money)

ui.run()
