import joblib
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel

linearRegression = joblib.load("./model/linearRegression.joblib")