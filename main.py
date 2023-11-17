from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import constants

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

ESTADOS = constants.estados
DETALHES = constants.detalhes

@app.get("/")
def home():
    return {"status": 200, "data": "API ESTADOS DO BRASIL ON"}

@app.get("/estados")
def estados():
    return {"status": 200, "data": ESTADOS}

@app.get("/estados/detalhes/{id}")
def get_detalhes(id: int):
    if id in DETALHES:
        return {"status": 200, "data": DETALHES[id]}
    else:
        return {"status": 400, "data": "Identificador de estado inválido"}
