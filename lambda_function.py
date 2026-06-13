"""
============================================================
  Mi Primera Lambda - "Motiv-AWS"  💜
============================================================
Una funcion Lambda que devuelve una pagina web bonita con un
mensaje motivacional para personas en tecnologia + un dato
curioso sobre AWS Lambda.

 - NO necesita servidores
 - NO necesita librerias externas (solo Python estandar)
 - Se ejecuta solo cuando alguien la llama
 - Cabe en la capa gratuita de AWS (Free Tier)

Como se usa:
  Se publica con una "Function URL" y se abre en el navegador.
  Opcional: agrega ?nombre=TuNombre al final de la URL para
  recibir un saludo personalizado.

Autora de la demo: Geraldinne Laruta
============================================================
"""

import json
import random
import datetime
import os

# --- Frases motivacionales para personas en tecnologia ---
FRASES = [
    "El codigo que escribes hoy es el superpoder de manana.",
    "No tienes que ser experta para empezar, pero tienes que empezar para ser experta.",
    "Cada error es una pista, no un fracaso.",
    "La nube no tiene limites... y tu tampoco.",
    "Construye cosas pequenas. Aprende cosas enormes.",
    "El mejor momento para aprender Lambda fue ayer. El segundo mejor es ahora.",
]

# --- Datos curiosos sobre AWS Lambda ---
DATOS_CURIOSOS = [
    "Lambda solo cobra por los milisegundos que tu codigo se ejecuta.",
    "Con la capa gratuita tienes 1 millon de ejecuciones GRATIS cada mes.",
    "No administras ni un solo servidor: AWS lo hace por ti.",
    "Una Lambda puede 'despertar' en milisegundos cuando alguien la llama.",
    "Lambda escala sola: de 1 usuario a 1 millon sin que muevas un dedo.",
    "Puedes escribir Lambdas en Python, Node.js, Java, Go, Ruby y mas.",
]


def lambda_handler(event, context):
    """
    Este es el punto de entrada. AWS llama a esta funcion
    automaticamente cada vez que alguien visita la URL.

    'event'   -> informacion de quien nos llama (parametros, etc.)
    'context' -> informacion del entorno de ejecucion de AWS
    """

    # 1) Intentamos leer el parametro ?nombre= de la URL (si existe)
    nombre = "futura crack de la nube"
    params = event.get("queryStringParameters") or {}
    if params.get("nombre"):
        nombre = params["nombre"]

    # 2) Elegimos una frase y un dato curioso al azar
    frase = random.choice(FRASES)
    dato = random.choice(DATOS_CURIOSOS)

    # 3) Datos que demuestran que SI se ejecuta en la nube de AWS
    region = os.environ.get("AWS_REGION", "desconocida")
    ahora = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

    # 4) Construimos una pagina HTML bonita como respuesta
    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Mi Primera Lambda</title>
  <style>
    body {{
      margin: 0;
      font-family: 'Segoe UI', system-ui, sans-serif;
      background: linear-gradient(135deg, #4B1E6B 0%, #7B2D8E 50%, #FF6B9D 100%);
      color: #ffffff;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
    }}
    .card {{
      background: rgba(255, 255, 255, 0.10);
      border: 1px solid rgba(255, 255, 255, 0.25);
      border-radius: 24px;
      padding: 48px 40px;
      max-width: 560px;
      text-align: center;
      backdrop-filter: blur(8px);
      box-shadow: 0 20px 60px rgba(0,0,0,0.35);
    }}
    .bolt {{ font-size: 64px; }}
    h1 {{ font-size: 30px; margin: 12px 0 4px; }}
    .hola {{ color: #FFD37E; }}
    .frase {{ font-size: 22px; font-style: italic; margin: 28px 0; line-height: 1.4; }}
    .dato {{
      background: rgba(255, 153, 0, 0.20);
      border-radius: 14px;
      padding: 16px 20px;
      font-size: 15px;
      margin-top: 24px;
    }}
    .dato b {{ color: #FF9900; }}
    .meta {{ margin-top: 28px; font-size: 12px; opacity: 0.75; }}
    .meta code {{ color: #FFD37E; }}
  </style>
</head>
<body>
  <div class="card">
    <div class="bolt">&#9889;</div>
    <h1>Hola, <span class="hola">{nombre}</span></h1>
    <p class="frase">&ldquo;{frase}&rdquo;</p>
    <div class="dato"><b>Dato curioso de Lambda:</b><br>{dato}</div>
    <div class="meta">
      Servida por <b>AWS Lambda</b> &middot; Region: <code>{region}</code><br>
      Hora del servidor: <code>{ahora}</code>
    </div>
  </div>
</body>
</html>"""

    # 5) Devolvemos la respuesta. AWS la entrega a quien nos llamo.
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "text/html; charset=utf-8"},
        "body": html,
    }
