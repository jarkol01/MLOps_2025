from fastapi import FastAPI

from api.models.schema import PredictRequest, PredictResponse
from inference import load_sentence_transformer, load_classifier, predict


app = FastAPI()

sentence_model = load_sentence_transformer()
classifier = load_classifier()


@app.post("/predict")
def predict_endpoint(request: PredictRequest) -> PredictResponse:
    prediction = predict(sentence_model, classifier, request.text)
    return PredictResponse(prediction=str(prediction))
