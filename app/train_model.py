import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

import pickle

df = pd.read_csv("../data/meal_health_labels.csv", sep="\t")

X = df[["calories", "protein", "carbs", "fat", "fiber"]]

y = df["label"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = DecisionTreeClassifier()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

with open("../models/meal_classifier.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved successfully")