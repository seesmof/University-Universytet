import random

from matplotlib import pyplot as plt

# generate ages
ages = [random.randint(40, 60) for age in range(10)]
ages = [min(ages) - 10] + ages + [max(ages) + 10]
ages = sorted(ages)
print(ages)

ages_indeces = [index for index in range(len(ages))]

# show ages
plt.scatter(x=ages, y=ages_indeces)
plt.title("Generated ages")
plt.xlabel("Age (years)")
plt.tight_layout()
plt.show()

# normalize ages
normalized_ages = list()
for index, age in enumerate(ages):
    value = age - min(ages)
    value /= max(ages) - min(ages)
    normalized_ages.append(round(value, 2))
print(normalized_ages)

# show normalized ages
plt.scatter(x=normalized_ages, y=ages_indeces)
plt.title("Normalized ages")
plt.xlabel("Age (years)")
plt.tight_layout()
plt.show()
