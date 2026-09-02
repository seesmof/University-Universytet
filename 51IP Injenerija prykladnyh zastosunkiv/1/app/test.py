data = [10, 30, 20, 40, 50]
predicted = [8, 28, 20, 39, 48]


def mae(original_data: list, predicted_values: list):
    if len(original_data) != len(predicted_values):
        raise ValueError("The lengths of the two given arrays are not equal.")

    differences = sum(
        abs(original - predicted)
        for original, predicted in zip(original_data, predicted_values)
    )
    return differences / len(original_data)


result = mae(data, predicted)
print(result)
