from matplotlib import pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_iris, make_blobs
from sklearn.linear_model import Perceptron
from sklearn.model_selection import train_test_split

n_samples = 500

data, labels = make_blobs(
    n_samples=n_samples,
    centers=([1.1, 3], [4.5, 6.9], [-1, 7]),
    cluster_std=1.3,
    random_state=0,
)

colors = ("green", "orange", "blue")
fig, ax = plt.subplots()
for n_class in range(3):
    ax.scatter(
        data[labels == n_class][:, 0],
        data[labels == n_class][:, 1],
        c=colors[n_class],
        s=50,
        label=str(n_class),
    )
# plt.show()

datasets = train_test_split(data, labels, test_size=0.2)
train_data, test_data, train_labels, test_labels = datasets

p = Perceptron(random_state=42)
p.fit(train_data, train_labels)

prediction_train = p.predict(train_data)
prediction_test = p.predict(test_data)
train_score = accuracy_score(prediction_train, train_labels)
print(f"Score on train data: {train_score}")
test_score = accuracy_score(prediction_test, test_labels)
print(f"Score on test data: {test_score}")
print(p.score(train_data, train_labels))
print(prediction_test)
