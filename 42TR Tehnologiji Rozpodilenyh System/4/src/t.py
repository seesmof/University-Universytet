import matplotlib.pyplot as plt

x = [
    20000,
    40000,
    60000,
    80000,
]
y = [
    0.00018030,
    0.00014770,
    0.00018110,
    0.00032590,
]

plt.scatter(x, y, c="magenta", marker="o")
# Або через plot для з'єднання лінією:
plt.plot(x, y, "m-o")
plt.show()
