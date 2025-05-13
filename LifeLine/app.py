
from fastapi import FastAPI

from src.operations.example import predict_location
from src.schemas.bg import Prediction
import uvicorn
import pickle



app = FastAPI(
    title="Ambulance Prediction API",
    description="API for predicting the location of an ambulance based on the hour of the day",
    version="0.1.0",
)


@app.get("/")
def home():
    return {
        "health_check": "OK",
        "model_version": "0.1.0"
    }


@app.post("/predict")
def predict_coordinates(data: Prediction):
    with open("src/models/kmeans.pkl", "rb") as f:
        model = pickle.load(f)
    data = predict_location(data.dict())
    prediction = model.predict(data)
    return {
        "prediction": prediction[0]
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)
