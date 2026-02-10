from nicegui import ui
import multiprocessing
from workers import power_worker

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


def montgomery(a: int, n: int, m: int) -> int:
    binary_N = int(bin(n)[2:])

    y1 = a % m
    y2 = (a * a) % m

    for k in range(binary_N - 2, 0, -1):
        bit = (n >> k) & 1

        if bit == 1:
            y1 = (y1 * y2) % m
            y2 = (y2 * y2) % m
        else:
            y1 = (y1 * y2) % m
            y2 = (y1 * y1) % m

    return y1


def ridge(a: int, n: int, m: int, p: int) -> int:
    if p < 1:
        p = 1

    # 1. Формування часткових показників (гребінь)
    s = [0] * p
    num_bits = n.bit_length()

    for k in range(num_bits):
        if (n >> k) & 1:
            processor_index = k % p
            s[processor_index] |= 1 << k

    # 2. Підготовка завдань
    tasks = [(a, partial_exp, m) for partial_exp in s]

    # 3. Паралельне виконання
    # Важливо: worker імпортовано з зовнішнього файлу
    results = []

    # Використовуємо контекстний менеджер для Pool
    with multiprocessing.Pool(processes=p) as pool:
        results = pool.map(power_worker, tasks)

    # 4. Об'єднання результатів
    final_result = 1
    for part_res in results:
        final_result = (final_result * part_res) % m

    return final_result


def handle_binary(base, exponent, modulus):
    result: int = binary(int(base), int(exponent), int(modulus))
    binary_output.value = result
    binary_output.update()


def handle_montgomery(base, exponent, modulus):
    result: int = montgomery(int(base), int(exponent), int(modulus))
    montgomery_output.value = result
    montgomery_output.update()


def handle_ridge(base, exponent, modulus, processors):
    result: int = ridge(int(base), int(exponent), int(modulus), int(processors))
    ridge_output.value = result
    ridge_output.update()


class TabNames:
    BINARY = "Binary"
    MONTGOMERY = "Montgomery"
    RIDGE = "Ridge"
    COMPARISON = "Comparison"


with ui.tabs().classes("w-full") as main_tabs:
    binary_tab = ui.tab(TabNames.BINARY)
    montgomery_tab = ui.tab(TabNames.MONTGOMERY)
    ridge_tab = ui.tab(TabNames.RIDGE)
    comparison_tab = ui.tab(TabNames.COMPARISON)
with ui.tab_panels(main_tabs, value=TabNames.BINARY).classes("w-full"):
    with ui.tab_panel(TabNames.BINARY):
        with ui.row():
            bin_base = ui.input(label="Base")
            bin_exponent = ui.input(label="Exponent")
            bin_modulus = ui.input(label="Modulus")
        ui.button(
            text="Calculate",
            on_click=lambda: handle_binary(
                bin_base.value, bin_exponent.value, bin_modulus.value
            ),
        ).classes("w-full")
        binary_output = ui.input(label="Result").classes("w-full")
    with ui.tab_panel(TabNames.MONTGOMERY):
        with ui.row():
            mont_base = ui.input(label="Base")
            mont_exponent = ui.input(label="Exponent")
            mont_modulus = ui.input(label="Modulus")
        ui.button(
            text="Calculate",
            on_click=lambda: handle_montgomery(
                mont_base.value, mont_exponent.value, mont_modulus.value
            ),
        ).classes("w-full")
        montgomery_output = ui.input(label="Result").classes("w-full")
    with ui.tab_panel(TabNames.RIDGE):
        with ui.row():
            ridge_base = ui.input(label="Base")
            ridge_exponent = ui.input(label="Exponent")
            ridge_modulus = ui.input(label="Modulus")
            ridge_processors = ui.input(label="Processors")
        ui.button(
            text="Calculate",
            on_click=lambda: handle_ridge(
                ridge_base.value,
                ridge_exponent.value,
                ridge_modulus.value,
                ridge_processors.value,
            ),
        ).classes("w-full")
        ridge_output = ui.input(label="Result").classes("w-full")
    with ui.tab_panel(TabNames.COMPARISON):
        ui.label("Comparison")


ui.run(title="TR2", favicon="🔬")
