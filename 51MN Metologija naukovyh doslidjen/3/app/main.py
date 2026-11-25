import bottleneck as bn
import pandas as pd
import numpy as np
import json
import os

# 1 Отримання даних
file_name = "komyshuvakha-weather.csv"
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "..", file_name)
data = pd.read_csv(file_path, sep=";")
print(f"Завантажені дані:\n{data}")

# 2 Перевірка
missing_values = data.isnull()
print(f"\nПеревірка на відсутні дані:\n{missing_values}")

# 3 Поділ або сценарії
needed_columns = "Дата,Середня".split(",")
data = data[needed_columns]
print(f"\nДані лише з потрібними стовпцями:\n{data}")

# 4 Попередня обробка
data["Дата"] = pd.to_datetime(data["Дата"], format="%d.%m.%Y")
print(f'\nДані після конвертування поля "Дата" у формат datetime:\n{data}')

# 5 Налаштування
data = data.rename(columns={"Дата": "Date", "Середня": "AvgTemp"})
print(f"\nДані після перейменування стовпців:\n{data}")

# 6 Запуск
WINDOW_SIZE = 3
result = bn.move_mean(data["AvgTemp"].to_numpy(), window=WINDOW_SIZE)
formatted_result = [0, 0] + [int(value) for value in result[2:]]
print(f"\nРезультат застосування ковзного середнього:\n{formatted_result}")
print(f"\nДовжина отриманого масиву:\n{len(formatted_result)}")

# 7 Метрики
initial_data = data["AvgTemp"].to_numpy()
result = np.array(formatted_result)
mae = np.mean(np.abs(initial_data - result))
print(f"\nОбчислена середня абсолютна похибка:\n{mae}")

# 8 Збереження результатів
results = {
    "initial_temperature": list(int(value) for value in initial_data),
    "moving_average_applied": formatted_result,
    "mae": mae,
}
output_file_name = "results.json"
output_file_path = os.path.join(current_dir, output_file_name)
with open(output_file_path, encoding="utf-8", mode="w") as f:
    json.dump(results, f)
print("\nДані записані у файл JSON.")
