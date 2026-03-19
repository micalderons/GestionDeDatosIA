from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="Gestión de Datos - Entorno IA",
    description="API básica desarrollada con FastAPI para despliegue en Render",
    version="1.0.0"
)

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Gestión de Datos - Entorno IA</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f6f8;
                color: #222;
                text-align: center;
                padding: 50px;
            }
            .card {
                max-width: 700px;
                margin: auto;
                background: white;
                padding: 30px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.12);
            }
            h1 {
                color: #0b57d0;
            }
            p {
                font-size: 18px;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                text-decoration: none;
                background: #0b57d0;
                color: white;
                padding: 12px 20px;
                border-radius: 8px;
            }
            a:hover {
                background: #084298;
            }
            ul {
                text-align: left;
                display: inline-block;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Gestión de Datos - Entorno IA</h1>
            <p>La aplicación se encuentra desplegada correctamente en Render.</p>
            <p>Este proyecto fue desarrollado con FastAPI, Docker, GitHub Actions y Render.</p>

            <ul>
                <li>API operativa</li>
                <li>Pipeline CI/CD funcionando</li>
                <li>Despliegue en la nube activo</li>
            </ul>

            <br>
            <a href="/docs">Ver documentación Swagger</a>
        </div>
    </body>
    </html>
    """

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