import pandas as pd
import numpy as np
import joblib

def load_model(file_path):
    return joblib.load(file_path)

data = pd.read_csv("predict_data.csv")
model = load_model('model.pkl')
predictions = model.predict(data)
print(predictions)