import joblib
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np


class IrisData(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float


model = joblib.load("model.pkl")  

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/health")
async def health():
    if model:
        return {"status": "ok"}
    else:
        return {"status": "error"}

@app.post("/predict")
async def predict(data: IrisData):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    prediction = model.predict(input_data)
    return {"prediction": int(prediction[0])}
    
# curl -X 'POST' \
#     'http://localhost:8000/predict' \
#     -H 'accept: application/json' \
#     -H 'Content-Type: application/json' \
#     -d "{\"sepal_length\": 5.1, \"sepal_width\": 3.5, \"petal_length\": 1.4, \"petal_width\": 0.2}"
