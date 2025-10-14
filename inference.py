import joblib
import os
from sentence_transformers import SentenceTransformer


def load_sentence_transformer(model_path: str = "models/sentence_transformer.model"):
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model not found at path: {model_path}")

    model = SentenceTransformer(model_path)
    return model


def load_classifier(classifier_path: str = "models/classifier.joblib"):
    if not os.path.exists(classifier_path):
        raise FileNotFoundError(f"Classifier not found at path: {classifier_path}")

    return joblib.load(classifier_path)


def predict(sentence_model, classifier, text: str):
    embeddings = sentence_model.encode([text])
    prediction = classifier.predict(embeddings)

    mapping = {0: "negative", 1: "neutral", 2: "positive"}

    return mapping[prediction[0]]
