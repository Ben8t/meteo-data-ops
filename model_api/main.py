from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


from io import StringIO


app = FastAPI()

class InputData(BaseModel):
    month_: int
    day_: int
    hour_: int
    temp_1: float
    temp_2: float
    temp_3: float
    temp_4: float
    station_id: str

def load_model(file_path):
    return joblib.load(file_path)


@app.get("/predict/")
async def predict(data: InputData):
    model = load_model('model.pkl')

    input_dict = {
        "month_": [data.month_],
        "day_": [data.day_],
        "hour_": [data.hour_],
        "temp_1": [data.temp_1],
        "temp_2": [data.temp_2],
        "temp_3": [data.temp_3],
        "temp_4": [data.temp_4],
        "station_id": [data.station_id]
    }

    input_df = pd.DataFrame(input_dict)
    prediction = model.predict(input_df)
    return {"prediction": prediction[0][0]}

# curl -X GET "http://localhost:8082/predict/?month_=5&day_=15&hour_=12&temp_1=25.5&temp_2=26.0&temp_3=24.8&temp_4=26.2&station_id=123"
