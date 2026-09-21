import pywinui as ui


class CounterApp(ui.App):
    def build(self):
        count = ui.TextBlock("0", font_size=32)


CounterApp().run()
