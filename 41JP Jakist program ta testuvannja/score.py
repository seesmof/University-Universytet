labs = {
    "1": 40,
    "2": 70,
    "3": 30,
    "4": 20,
    "5": 20,
    "6": 60,
    "7": 20,
    "8": 70,
    "9": 50,
    "10": 30,
    "11": 30,
    "12": 20,
}
rgz = 20
test = 70

labs_result = sum(labs.values()) / 12
rgz_result = rgz * 0.25
test_result = test * 0.25

result = labs_result + rgz_result + test_result
print(result)
