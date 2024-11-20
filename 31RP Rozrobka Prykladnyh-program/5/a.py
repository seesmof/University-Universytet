from nicegui import ui, app
app.add_static_files('/images', '.')

ui.image('/images/image.jpg')

ui.run()