from nicegui import ui 

with ui.dialog() as result,ui.card():
    ui.label('ALLELUJAH')
    ui.button('AMEN',on_click=result.close)

ui.button('AMEN',on_click=result.open)
ui.run()