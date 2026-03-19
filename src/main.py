from fastapi import FastAPI
import os

app = FastAPI(
    title="Gestión de Datos - Entorno IA",
    description="API básica desarrollada con FastAPI para despliegue en Render",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "mensaje": "API desplegada correctamente en Render",
        "estado": "ok"
    }

@app.get("/saludo")
def saludo():
    return {
        "mensaje": "Hola, esta es una API de prueba usando FastAPI"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }