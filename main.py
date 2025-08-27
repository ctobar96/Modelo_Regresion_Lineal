import joblib
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging

linearRegression = joblib.load("./model/linearRegression.joblib")

 # crea un logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def predict_price_continuous(features: np.ndarray) -> float:
    """
    Devuelve un valor continuo predicho por un modelo de regresión lineal.

    Args:
      features: array 1D con n_features (shape: (n_features,))

    Returns:
      Valor numérico predicho (float).
    """
    # Asegura la forma (1, n_features)
    X = features.reshape(1, -1)
    
    try:
        # predict() devuelve un array, tomamos el primer elemento
        raw_pred = linearRegression.predict(X)[0]
        pred_value = float(raw_pred)  # JSON-friendly
        return pred_value

    except ValueError as ve:
        logger.error(
            "predict_price_continuous: shape mismatch. "
            "Esperado (%d,), recibido %s",
            linearRegression.coef_.shape[0],
            features.shape,
        )
        raise HTTPException(status_code=422, detail="Invalid feature vector shape")

    except Exception as exc:
        logger.exception("Error al predecir precio de regresión")
        raise HTTPException(status_code=500, detail="Error interno del servidor")
  

# Asignamos una instancia de la clase FastAPI a la variable "app".
# Interacturaremos con la API usando este elemento.
app = FastAPI(title="Modelo de Regresión Lineal - FastAPI")


# Creamos una clase para el vector de features de entrada
class Item(BaseModel):
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
        "message": "✅ API lista",
        "docs": "http://localhost:8000/docs",
        "Proyecto GitHub": "https://github.com/ctobar96/Modelo_Regresion_Lineal.git"
    }

# ----------------------------------------------------------------------------------------------------------
# Este endpoint maneja la lógica para estimar
@app.post("/predict_price")
def prediction(item: Item, confidence: float):
    
    # Correr el modelo de Regresión lineal
    arr = np.array([item.area, item.bedrooms, item.bathrooms, item.stories, item.guestroom, 
                                item.hotwaterheating, item.airconditioning, item.parking])

    price = predict_price_continuous(arr)
        
    # Retornar el resultado de la predicción
    return {'predicted_price': price}

# ----------------------------------------------------------------------------------------------------------



