import os
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.ensemble import RandomForestClassifier
from sklearn.impute import KNNImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC

current_folder = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_folder, "..", "train.csv")
df = pd.read_csv(file_path)

# Remove unnecessary columns
unnecessary = "PassengerId,Pclass,SibSp,Parch,Ticket,Fare,Cabin,Embarked".split(",")
df = df.drop(unnecessary, axis=1)
print(df)

# Remove name
df = df.drop("Name", axis=1)
# Count missing values
print(df.isnull().sum())

# Convert gender to 0 and 1
le = LabelEncoder()
df["Sex"] = le.fit_transform(df["Sex"])

# Replace missing ages with average
imputer = KNNImputer(n_neighbors=7)
df["Age"] = imputer.fit_transform(df[["Age"]]).ravel()
print(df)

# Split dataset
target_feature = df.Survived.to_numpy()
survived_scores = pd.DataFrame(target_feature, columns=["Survived"])
df = df.drop(["Survived"], axis=1)
X_train, X_test, y_train, y_test = train_test_split(df, target_feature)

# Modeling results
kmeans_model = KMeans()
kmeans_model.fit(X_train)
kmeans_results = kmeans_model.predict(X_test)
print(f"{kmeans_model.cluster_centers_ = }")
print(f"{kmeans_results = }")

kneighbors_model = KNeighborsClassifier(n_neighbors=7)
kneighbors_model.fit(X_train, y_train)
kneighbors_results = kneighbors_model.predict(X_test)
print(f"{kneighbors_results = }")

forest_model = RandomForestClassifier()
forest_model.fit(X_train, y_train)
forest_results = forest_model.predict(X_test)
print(f"{forest_results = }")

logistic_model = LogisticRegression()
logistic_model.fit(X_train, y_train)
logistic_results = logistic_model.predict(X_test)
print(f"{logistic_results = }")

svc_model = SVC()
svc_model.fit(X_train, y_train)
svc_results = svc_model.predict(X_test)
print(f"{svc_results = }")

# Comparing models
testing_indeces = list(X_test.index)
corrects = [int(survived_scores.iloc[i].Survived) for i in testing_indeces]

# Plotting graphs
models = ["KNeighbors", "RandomForest", "Logistic", "SVC"]
accuracies = [
    sum([int(abs(corrects[i] - model_result[i])) for i in range(len(corrects))])
    for model_result in [
        kneighbors_results,
        forest_results,
        logistic_results,
        svc_results,
    ]
]

resulting_dictionary = dict()
for index in range(len(models)):
    m = models[index]
    a = accuracies[index] / len(testing_indeces)
    resulting_dictionary[m] = a
print("Errors in each model:", resulting_dictionary)
plt.title("Number of errors in each model")
plt.bar(models, accuracies, color="g")
plt.show()
