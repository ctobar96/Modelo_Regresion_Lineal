import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
import logging

linearRegression = joblib.load("./model/linearRegression.joblib")

 # crea un logger
+logging.basicConfig(level=logging.INFO)
+logger = logging.getLogger(__name__)

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
# ----------------------------------------------------------------------------------------------------------
# Usando @app.get("/") definimos un método GET para el endpoint / (que sería como el "home")
@app.get("/")
def home():
    return {
        "message": "Service up ✅",
        "endpoints": {
            "docs": "http://localhost:8000/docs"
        }
    }

# ----------------------------------------------------------------------------------------------------------
# Este endpoint maneja la lógica para estimar
@app.post("/predict")
def prediction(item: Item, confidence: float):
    try:
        # Correr el modelo de Regresión lineal
        features_trip = np.array([item.price, item.area, item.bedrooms, item.bathrooms, item.stories, item.guestroom, 
                                item.hotwaterheating, item.airconditioning, item.parking])

        pred = predict_price(features_trip, confidence)
        logger.info(f"Predicción realizada: {pred} con confianza {confidence}")
        
        # Transmitir la respuesta de vuelta al cliente
        
        # Retornar el resultado de la predicción
        return {'predicted_class': pred}
    except Exception as e:
        logger.error(f"Error en /predict: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno en la predicción")

# ----------------------------------------------------------------------------------------------------------
#DATOS DE ENTRADA
item_features = {
    "price": 15210000,
    "area": 8502, 
    "bedrooms": 5,
    "bathrooms": 2,
    "stories": 2,
    "guestroom": 0,
    "hotwaterheating": 1,
    "airconditioning": 0,
    "parking": 2
}

url = "https://modelo-regresion-lineal.onrender.com/predict"

resp = requests.post(
    url, 
    json=item_features
)
resp.raise_for_status()
print("Predicción:", resp.json()["predicted_class"])
