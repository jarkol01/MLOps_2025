from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import joblib


def load_data():
    return datasets.load_iris()


def train_model():
    iris = load_data()
    X = iris.data
    y = iris.target
    knn = KNeighborsClassifier()
    knn.fit(X, y)
    return knn


def save_model():
    knn = train_model()
    joblib.dump(knn, "knn.joblib")
