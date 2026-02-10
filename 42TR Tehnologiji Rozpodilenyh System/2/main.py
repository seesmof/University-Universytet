import time
from nicegui import ui
import multiprocessing
from workers import power_worker

with ui.card().classes("mx-auto"):
    ui.label(
        "Так бо Бог полюбив світ, що дав Сина Свого Однородженого, щоб кожен, хто вірує в Нього, не згинув, але мав життя вічне. (Йоан 3:16)"
    )


def binary(a: int, n: int, m: int) -> int:
    if m == 1:
        return 0

    result = 1
    a = a % m  # Обробляємо випадок, коли база більша за модуль

    while n > 0:
        # Якщо поточний біт (наймолодший) дорівнює 1
        if n % 2 == 1:
            result = (result * a) % m

        # Підносимо базу до квадрата і зсуваємо степінь вправо
        a = (a * a) % m
        n //= 2

    return result


def montgomery(a: int, n: int, m: int) -> int:
    binary_N = int(bin(n)[2:])

    y1 = a % m
    y2 = (a * a) % m

    for i in range(binary_N - 2, 0, -1):
        bit = (n >> i) & 1

        if bit == 1:
            y1 = (y1 * y2) % m
            y2 = (y2 * y2) % m
        else:
            y1 = (y1 * y1) % m
            y2 = (y1 * y2) % m

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


def calculate_times():
    base = 3
    exponent = 10
    modulus = 7
    processors = 4

    binary_start = time.perf_counter()
    binary(base, exponent, modulus)
    binary_end = time.perf_counter()
    binary_time = binary_end - binary_start

    montgomery_start = time.perf_counter()
    montgomery(base, exponent, modulus)
    montgomery_end = time.perf_counter()
    montgomery_time = montgomery_end - montgomery_start

    ridge_start = time.perf_counter()
    ridge(base, exponent, modulus, processors)
    ridge_end = time.perf_counter()
    ridge_time = ridge_end - ridge_start

    data = [
        {"method": TabNames.BINARY, "time": binary_time},
        {"method": TabNames.MONTGOMERY, "time": montgomery_time},
        {"method": TabNames.RIDGE, "time": ridge_time},
    ]
    comparison_table.update_rows(data)


class TabNames:
    BINARY = "Бінарний"
    MONTGOMERY = "Монтгомері"
    RIDGE = "Гребінь"
    COMPARISON = "Порівняння"


with ui.tabs().classes("w-full") as main_tabs:
    binary_tab = ui.tab(TabNames.BINARY)
    montgomery_tab = ui.tab(TabNames.MONTGOMERY)
    ridge_tab = ui.tab(TabNames.RIDGE)
    comparison_tab = ui.tab(TabNames.COMPARISON)
with ui.tab_panels(main_tabs, value=TabNames.BINARY).classes("w-full"):
    with ui.tab_panel(TabNames.BINARY):
        with ui.row():
            bin_base = ui.input(label="Основа")
            bin_exponent = ui.input(label="Експонент")
            bin_modulus = ui.input(label="Модуль")
        ui.button(
            text="Розрахувати",
            on_click=lambda: handle_binary(
                bin_base.value, bin_exponent.value, bin_modulus.value
            ),
        ).classes("w-full")
        binary_output = ui.input(label="Результат").classes("w-full")
    with ui.tab_panel(TabNames.MONTGOMERY):
        with ui.row():
            mont_base = ui.input(label="Основа")
            mont_exponent = ui.input(label="Експонент")
            mont_modulus = ui.input(label="Модуль")
        ui.button(
            text="Розрахувати",
            on_click=lambda: handle_montgomery(
                mont_base.value, mont_exponent.value, mont_modulus.value
            ),
        ).classes("w-full")
        montgomery_output = ui.input(label="Результат").classes("w-full")
    with ui.tab_panel(TabNames.RIDGE):
        with ui.row():
            ridge_base = ui.input(label="Основа")
            ridge_exponent = ui.input(label="Експонент")
            ridge_modulus = ui.input(label="Модуль")
            ridge_processors = ui.input(label="Процесорів")
        ui.button(
            text="Розрахувати",
            on_click=lambda: handle_ridge(
                ridge_base.value,
                ridge_exponent.value,
                ridge_modulus.value,
                ridge_processors.value,
            ),
        ).classes("w-full")
        ridge_output = ui.input(label="Результат").classes("w-full")
    with ui.tab_panel(TabNames.COMPARISON):
        ui.button(text="Протестувати", on_click=lambda: calculate_times())
        cols = [
            {
                "name": "Method",
                "label": "Метод",
                "field": "method",
                "required": True,
                "align": "left",
            },
            {"name": "Time", "label": "Час", "field": "time", "required": True},
        ]
        data = [
            {"method": TabNames.BINARY, "time": 0.0},
            {"method": TabNames.MONTGOMERY, "time": 0.0},
            {"method": TabNames.RIDGE, "time": 0.0},
        ]
        comparison_table = ui.table(
            columns=cols,
            rows=data,
            row_key="method",
        )

ui.run(title="ТР2. Алгоритми піднесення до степеня", favicon="📈")
