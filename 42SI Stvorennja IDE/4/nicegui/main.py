from nicegui import ui, app


ui.textarea(placeholder="Your code here...").props("outlined").classes(
    "w-full"
).bind_value_to(app.storage.general, "input")
ui.textarea().props("outlined disable").classes("w-full")
ui.button("Run").classes("w-full").props("outline")

value = app.storage.general["input"]
print(value)

ui.run(title="Rust IDE", favicon="🚜")
