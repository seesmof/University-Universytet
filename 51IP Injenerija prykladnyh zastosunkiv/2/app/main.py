data = [
    24,
    56,
    82,
    88,
    85,
    29,
    69,
    91,
    30,
    76,
    58,
]

size = round(len(data) * 0.8)
train = data[:size]
test = data[size:]

print(train, test)
