from fastapi import FastAPI
import numpy as np

from api.models.iris import PredictRequest, PredictResponse
from inference import load_model, predict


app = FastAPI()
model = load_model()


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict_endpoint(request: PredictRequest) -> PredictResponse:
    data = np.array(list(request.model_dump().values())).reshape(1, -1)
    prediction = predict(model, data)
    return PredictResponse(prediction=prediction)
