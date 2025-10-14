import joblib
import os

from training import save_model


def load_model():
    if not os.path.exists("knn.joblib"):
        save_model()
    return joblib.load("knn.joblib")


def predict(model, data):
    prediction = model.predict(data)

    species_names = ["setosa", "versicolor", "virginica"]
    labels = [species_names[pred] for pred in prediction]
    return labels[0] if len(labels) == 1 else labels
