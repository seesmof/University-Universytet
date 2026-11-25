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
experiment_results: list[dict] = list()
for experiment in range(EXPERIMENTS_COUNT):
    generated_data = []
    for _ in range(MEASUREMENTS_COUNT):
        given_number = random.randint(MIN_VALUE, MAX_VALUE)
        generated_data.append(given_number)

    meaned_data = bn.move_mean(np.array(generated_data), window=WINDOW_SIZE)
    resulting_list = [0, 0] + [int(value) for value in meaned_data[2:]]

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
    experiment_results.append(results)
output_file_name = "experiment_results.json"
output_file_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), output_file_name
)
with open(output_file_path, encoding="utf-8", mode="w") as f:
    json.dump(experiment_results, f)
