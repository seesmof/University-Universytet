from matplotlib import pyplot as plt


one=[2, 1, 2, 0, 0, 2, 2, 0, 0, 2, 0, 1, 0, 1, 2, 1, 0, 2, 1, 1, 2, 0, 0, 2, 0, 2, 0, 0, 1, 0, 2, 0, 1, 1, 2, 0, 2, 0]
two=[1, 2, 1, 0, 0, 1, 1, 0, 0, 1, 0, 2, 0, 2, 2, 2, 0, 1, 2, 2, 1, 0, 0, 1, 0, 1, 0, 0, 2, 0, 1, 0, 2, 2, 1, 0, 1, 0]
colors=list(set(one+two))
print(colors)

plt.scatter(one,two,cmap='viridis')
plt.show()