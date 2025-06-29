from collections import namedtuple
import random
import pandas as pd

# Визначити кількість екземплярів
rows = 2

# Перекладач сортів винограду
# 0 = білий, 1 = червоний
grape_kinds = {0: "white", 1: "red"}

# Визначити шаблон екземпляру
Grape = namedtuple("Grape", "kind,tss,ta,ph")

# Створити вибірку
grapes = [
    Grape(
        # Сорт або білий або червоний
        kind=random.choice([0, 1]),
        # Кількість розчинних твердих від 17 до 27
        tss=random.randint(17, 27),
        # Змінна кислотність від 6 до 17
        ta=random.randint(6, 17),
        # Кислотність від 2.8 до 4.0 з одним знаком після коми
        ph=round(random.uniform(2.8, 4.0), 1),
    )
    # Стільки разів, скільки написано в змінній rows
    for row in range(rows)
]

# Перетворити вибірку на таблицю даних
df = pd.DataFrame(grapes, columns=Grape._fields)

# Вивести таблицю
print(df)

import math


def get_mean(data: list[int]) -> float:
    # Порахувати суму всіх значень
    sum_of_data = sum(data)

    # Повернути суму поділену на кількість значень
    return sum_of_data / len(data)


def get_standard_deviation(data: list) -> float:
    # Отримати середнє значення ознаки
    mean = get_mean(data=data)

    # Порахувати різниці між кожним елементом і середнім значенням
    # Піднести до квадрату
    squares = [(element - mean) ** 2 for element in data]
    print(squares)

    # Отримати середнє значення з порахованих різниць
    average = get_mean(squares)

    # Повернути квадратний корінь середнього значення
    return math.sqrt(average)


for column_name, column_data in df.items():
    # Пропустити сорт винограду
    if column_name == "kind":
        continue

    # Перетворити цілочисельні на плаваючі коми
    df[column_name] = df[column_name].astype(float)

    # Отримати середнє значення ознаки та стандартне відхилення
    column_mean = get_mean(column_data.to_list())
    column_std = get_standard_deviation(column_data.to_list())
    print(column_data.to_list(), column_std)

    # Отримати номер екземпляру (index) та його значення (value)
    for row_index, row_value in enumerate(column_data):
        # Порахувати різницю між цим значенням і середнім по всій ознаці
        numerator = row_value - column_mean

        # Поділити різницю та стандартне відхилення ознаки
        result = numerator / column_std

        # Змінити це значення в таблиці на пораховане
        df.at[row_index, column_name] = result

# Вивести таблицю
print(df)

# Створити список класів зі стовпця сортів винограду
target = df["kind"].to_list()

# Зберегти лише унікальні значення класів
target = list(set(target))

# Прибрати стовпець сорту з таблиці
# df = df.drop("kind", axis=1)

centers = list()
for target_value in target:
    print(grape_kinds[target_value])
    center = dict()
    appropriate_data = df[df.kind == target_value]
    for column_name, column_data in appropriate_data.items():
        if column_name == "kind":
            continue
        point = get_mean(column_data.to_list())
        center[column_name] = point
    print(center)
