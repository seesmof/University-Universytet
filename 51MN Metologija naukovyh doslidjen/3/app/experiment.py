import bottleneck as bn
import numpy as np
import random
import json
import os

EXPERIMENTS_COUNT = 5
MEASUREMENTS_COUNT = 30
MIN_VALUE = -10
MAX_VALUE = 20
WINDOW_SIZE = 3
print(f"\nКількість проходів експерименту (бюджет): {EXPERIMENTS_COUNT}")

experiment_results: list[dict] = list()
for experiment in range(EXPERIMENTS_COUNT):
    print(f"\n\nЕксперимент №{experiment+1}")
    generated_data = []
    for _ in range(MEASUREMENTS_COUNT):
        given_number = random.randint(MIN_VALUE, MAX_VALUE)
        generated_data.append(given_number)
    print(f"\nПочатково згенеровані дані:\n{generated_data}")

    meaned_data = bn.move_mean(np.array(generated_data), window=WINDOW_SIZE)
    resulting_list = [0, 0] + [int(value) for value in meaned_data[2:]]
    print(f"\nДані після застосування ковзного середнього:\n{resulting_list}")

    generated_data = np.array(generated_data)
    meaned_data = np.array(resulting_list)

    mae = np.mean(np.abs(generated_data - meaned_data))
    mse = ((meaned_data - generated_data) ** 2).mean()
    rmse = np.sqrt(mse)

    results = {
        "mae": f"{mae:.2f}",
        "mse": f"{mse:.2f}",
        "rmse": f"{rmse:.2f}",
    }
    print(f"\nМетрики:\n{results}")
    experiment_results.append(results)

output_file_name = "experiment_results.json"
output_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), output_file_name
)
with open(output_file_path, encoding="utf-8", mode="w") as f:
    json.dump(experiment_results, f)
