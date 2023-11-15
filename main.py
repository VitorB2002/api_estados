from fastapi import FastAPI
import constants

app = FastAPI()

@app.get("/")
def home():
    return {"status": 200, "data": "API ESTADOS DO BRASIL ON"}

@app.get("/estados")
def estados():
    return constants.estados
