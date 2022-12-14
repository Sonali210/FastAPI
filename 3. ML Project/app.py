import uvicorn
from fastapi import FastAPI
import numpy as np
import pickle
import pandas as pd
from pydantic import BaseModel
class BankNote(BaseModel):
    variance: float 
    skewness: float 
    curtosis: float 
    entropy: float

app = FastAPI()
pickle_in = open("model.pkl","rb")
classifier=pickle.load(pickle_in)


@app.get('/')
def index():
    return {'message': 'Hello, World'}

@app.post('/predict')
def predict_banknote(data:BankNote):
    data = data.dict()
    variance=data['variance']
    skewness=data['skewness']
    curtosis=data['curtosis']
    entropy=data['entropy']
    prediction = classifier.predict([[variance,skewness,curtosis,entropy]])
    if(prediction[0]>0.5):
        prediction="Fake note"
    else:
        prediction="Its a Bank note"
    return {
        'prediction': prediction
    }
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
