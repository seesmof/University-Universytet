from nicegui import app, ui


def add_verse():
    # get values from inputs
    reference = ref.value.strip()
    content = text.value.strip()
    if reference and content:
        app.storage.general[reference] = content
        ref.value = ""
        text.value = ""
        verse_grid.refresh()


with ui.row().classes("w-full"):
    ref = ui.input(
        label="Verse reference",
        placeholder="John 3:16",
    )
    text = ui.input(
        label="Verse text",
        placeholder="For God so loved the world...",
    )
    ui.button("Add", on_click=add_verse)


# make grid reactive so it updates when storage changes
@ui.refreshable
def verse_grid():
    with ui.grid(columns=3).classes("gap-4"):
        for reference, content in app.storage.general.items():
            with ui.card():
                ui.label(reference).classes("text-lg font-bold")
                ui.label(content).classes("mt-2")


verse_grid()

ui.run(title="Vigenere", favicon="🔑")
