from math import log10


def load_data():
    import json

    with open("l1/data.json", "r", encoding="utf-8") as f:
        return json.load(f)


def get_intervals_count(dataset):
    return 1 + 3.322 * log10(len(dataset))


def get_mathematical_expectation(dataset):
    return sum(dataset) / len(dataset)


def get_dispersion(dataset):
    mean = get_mathematical_expectation(dataset)
    return sum((x - mean) ** 2 for x in dataset) / len(dataset)


def get_standard_deviation(dataset):
    return get_dispersion(dataset) ** 0.5


def get_range(dataset):
    return max(dataset) - min(dataset)


def get_interval_size(scope, intervals_count):
    return scope / intervals_count


dataset = load_data().get("one_three_array")

intervals_count = get_intervals_count(dataset)
math_expectation = get_mathematical_expectation(dataset)
dispersion = get_dispersion(dataset)
standard_deviation = get_standard_deviation(dataset)
data_range = get_range(dataset)
interval_size = get_interval_size(data_range, intervals_count)


def get_intervals():
    intervals = []
    for i in range(int(intervals_count)):
        lower_bount = min(dataset) + i * interval_size
        upper_bount = lower_bount + interval_size
        mean = (lower_bount + upper_bount) / 2
        occurence_frequency = 0
        for x in dataset:
            if x >= lower_bount and x < upper_bount:
                occurence_frequency += 1

        print(occurence_frequency)


intervals = get_intervals()
