#!/bin/bash
echo "> Lancement l'environnement virtuel python"
source ./pyvenv/bin/activate
echo "> Démarrage du serveur web"
uvicorn main:app & 