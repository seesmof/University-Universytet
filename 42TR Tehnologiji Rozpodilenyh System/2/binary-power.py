from nicegui import ui

"""
Реалізувати бінарний метод модульного піднесення до степені.
"""


def power_modular(a, n, m):
    """
    Обчислює (a^e)%m за допомогою бінарного методу.

    - a: основа, base
    - n: ступінь, exponent
    - m: модуль, modulus
    """

    if m == 1:
        return 0
    result = 1
    a = a % m
    while n > 0:
        if n % 2 == 1:  # Якщо exponent непарний
            result = (result * a) % m
        n = n // 2  # Ділимо exponent навпіл
        a = (a * a) % m  # Підносимо основу до квадрата
    return result


# Приклад використання: (3^13)%7 = 1594323%7 = 3
base = 3
exponent = 13
modulus = 7
print(f"({base}^{exponent}) % {modulus} = {power_modular(base, exponent, modulus)}")


def handleClick():
    result = power_modular(
        base_textbox.value, exponent_textbox.value, modulus_textbox.value
    )
    output_textbox.set_value(result)
    output_textbox.update()


@ui.refreshable
def render_ui():
    with ui.card().classes("mt-64 mx-auto"):
        with ui.row():
            base_textbox = ui.input("Base").bind_value_to(base)
            exponent_textbox = ui.input("Exponent").bind_value_to(exponent)
            modulus_textbox = ui.input("Modulus").bind_value_to(modulus)
        ui.button(
            "Calculate",
            on_click=lambda: handleClick,
        ).classes("w-full")
    with ui.card().classes("mt-4 mx-auto"):
        output_textbox = ui.input(label="Results")


render_ui()
ui.run(title="TR2. Binary Modulo", favicon="✝")
