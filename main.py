from fastapi import FastAPI
import constants

app = FastAPI()
ESTADOS = constants.estados
DETALHES = constants.detalhes

@app.get("/")
def home():
    return {"status": 200, "data": "API ESTADOS DO BRASIL ON"}

@app.get("/estados")
def estados():
    return ESTADOS

@app.get("/estados/detalhes/{id}")
def get_detalhes_estado(id: int):
    return DETALHES[id]
