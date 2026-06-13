"""
test_local.py
------------------------------------------------------------
Prueba la Lambda EN TU COMPUTADORA, sin subirla a AWS todavia.
Simula la llamada que hace AWS y guarda la respuesta como un
archivo .html que puedes abrir en tu navegador.

Como ejecutarlo (en la terminal, dentro de la carpeta proyecto):

    python test_local.py

Luego abre el archivo "salida.html" que se genera.
------------------------------------------------------------
"""

import json
from lambda_function import lambda_handler

# 1) Cargamos un evento de ejemplo (como el que enviaria AWS)
with open("event_ejemplo.json", "r", encoding="utf-8") as f:
    event = json.load(f)

# 2) Llamamos a la funcion igual que lo haria AWS
respuesta = lambda_handler(event, None)

# 3) Mostramos el resultado en la terminal
print("=" * 50)
print("STATUS CODE:", respuesta["statusCode"])
print("HEADERS:", respuesta["headers"])
print("=" * 50)

# 4) Guardamos el HTML para abrirlo en el navegador
with open("salida.html", "w", encoding="utf-8") as f:
    f.write(respuesta["body"])

print("Listo! Abre el archivo 'salida.html' en tu navegador.")
