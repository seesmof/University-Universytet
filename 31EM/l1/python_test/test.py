from random import randint

dataset = [randint(50, 100) for _ in range(100)]

data_range = max(dataset) - min(dataset)
intervals_count = 5
interval_width = data_range / intervals_count

intervals = []
for i in range(intervals_count):
    lower_bount = min(dataset) + i * interval_width
    upper_bount = lower_bount + interval_width
    mean = (lower_bount + upper_bount) / 2
    occurence_frequency = 0
    for x in dataset:
        if x >= lower_bount and x < upper_bount:
            occurence_frequency += 1

    print(occurence_frequency)
