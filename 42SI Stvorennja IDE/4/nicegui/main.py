from nicegui import ui

ui.textarea(placeholder="Your code here...").props("outlined").classes("w-full")
ui.textarea().props("outlined disable").classes("w-full")
ui.button("Run").classes("w-full").props("outline")

ui.run(title="Rust IDE", favicon="🚜")
