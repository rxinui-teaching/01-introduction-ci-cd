"""API REST code source

@author Rxinui
"""
import json
from typing import Optional
from fastapi import FastAPI, HTTPException

app = FastAPI()
with open("./ecoles.json") as fp:
    ECOLES = json.load(fp)


@app.get("/")
def root():
    return {
        "message": "Bienvenue à l'atelier 1. Cette API liste les écoles d'ingénieurs de Toulouse.",
        "routes": {
            "/ecoles": {
                "GET": {
                    "description": "Liste toutes les écoles d'ingénieurs de Toulouse"
                }
            },
            "/ecoles?groupe={groupe}": {
                "GET": {
                    "description": "Liste toutes les écoles d'ingénieurs d'un {groupe} donné (ie. INP, UT...)",
                    "argument": "groupe",
                }
            },
            "/ecoles/{ecole_id}": {
                "GET": {
                    "description": "Retourne l'école de l'{ecole_id} donné. L'{ecole_id} est un nombre allant de 1 à 10 (nombre totale d'écoles)"
                }
            },
        },
    }


@app.get("/ecoles")
def ecoles(groupe: Optional[str] = None):
    return (
        {_id: ecole for _id, ecole in ECOLES.items() if ecole["groupe"] == groupe}
        if groupe
        else ECOLES
    )


@app.get("/ecoles/{ecole_id}")
def ecole_par_id(ecole_id: str):
    ecole = ECOLES.get(ecole_id)
    if not ecole:
        raise HTTPException(
            status_code=404,
            detail=f"Ecole pour id={ecole_id} est inexistante dans notre base de données.",
        )
    return ecole
