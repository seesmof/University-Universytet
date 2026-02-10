from nicegui import ui

with ui.card().classes("mx-auto"):
    ui.label(
        "Так бо Бог полюбив світ, що дав Сина Свого Однородженого, щоб кожен, хто вірує в Нього, не згинув, але мав життя вічне. (Йоан 3:16)"
    )


def binary(a: int, n: int, m: int) -> int:
    """
    Бінарний метод піднесення до степені.

    :param a: base
    :type a: int
    :param n: exponent
    :type n: int
    :param m: modulus
    :type m: int
    """

    if n == 0:
        return 1
    if n == 1:
        return a % m

    binary_N = int(bin(n)[2:])
    y = a % m

    for k in range(binary_N - 2, 0, -1):
        y = (y * y) % m

        if (n >> k) & 1:
            y = (y * a) % m

    return y


def handle_binary(base, exponent, modulus):
    result: int = binary(int(base), int(exponent), int(modulus))
    binary_output.value = result
    binary_output.update()
    print(result)


class TabNames:
    BINARY = "Binary"
    MONTGOMERY = "Montgomery"
    RIDGE = "Ridge"


with ui.tabs().classes("w-full") as main_tabs:
    binary_tab = ui.tab(TabNames.BINARY)
    montgomery_tab = ui.tab(TabNames.MONTGOMERY)
    ridge_tab = ui.tab(TabNames.RIDGE)
with ui.tab_panels(main_tabs, value=TabNames.BINARY).classes("w-full"):
    with ui.tab_panel(TabNames.BINARY):
        with ui.row():
            base = ui.input(label="Base")
            exponent = ui.input(label="Exponent")
            modulus = ui.input(label="Modulus")
        ui.button(
            text="Calculate",
            on_click=lambda: handle_binary(base.value, exponent.value, modulus.value),
        ).classes("w-full")
        binary_output = ui.input(label="Result").classes("w-full")
    with ui.tab_panel(TabNames.MONTGOMERY):
        ui.label("Montgomery")
    with ui.tab_panel(TabNames.RIDGE):
        ui.label("Ridge")

ui.run(title="TR2", favicon="🔬")
