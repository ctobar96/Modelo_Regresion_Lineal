import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

linearRegression = joblib.load("./model/linearRegression.joblib")



def predict_price(features_trip, confidence=0.5):
    """Recibe un vector de características de hospedaje y predice 
       si el hospedaje tiene un valor alto.

    Argumentos:
        features_trip (array): Características del hospedaje, vector de tamaño 11.
        confidence (float, opcional): Nivel de confianza. Por defecto es 0.5.
    """
    
    pred_value = linearRegression.predict_proba(features_trip.reshape(1, -1))[0][1]
    if pred_value >= confidence:
      return 1
    else:
      return 0
  

# Asignamos una instancia de la clase FastAPI a la variable "app".
# Interacturaremos con la API usando este elemento.
app = FastAPI(title='Implementando un modelo de Machine Learning usando FastAPI')


# Creamos una clase para el vector de features de entrada
class Item(BaseModel):
    price: int
    area: int
    bedrooms: int
    bathrooms: int
    stories: int
    guestroom: int
    hotwaterheating: int
    airconditioning: int
    parking: int
"""
    "guestroom":{
        "yes": 0,
        "no": 1
    },
    "hotwaterheating":{
        "yes": 0,
        "no": 1 
    },
    "airconditioning":{
        "yes": 0,
        "no": 1 
    }

"""
# -----------------------------------------
# Usando @app.get("/") definimos un método GET para el endpoint / (que sería como el "home")
@app.get("/")
def home():
    return {
        "message": "Service up ✅",
        "endpoints": {
            "docs": "http://localhost:8000/docs"
        }
    }




