# ⚡ Hands-on with AWS Lambda 💜

Materiales de la charla **"Hands-on with AWS Lambda"** — aprende a crear tu primera
función Lambda en la nube, **sin servidores** y **sin pagar nada**.

> Por **Geraldinne Laruta**

## 📦 ¿Qué hay aquí?

| Archivo | Qué es |
|---|---|
| `Hands-on with AWS Lambda.pptx` | La presentación (23 slides). |
| `Guia-Paso-a-Paso.md` | Guía completa para subir el proyecto a AWS, paso a paso. |
| `Chuleta-Asistentes.pdf` | Resumen de una página para imprimir o compartir. |
| `proyecto/` | El proyecto de ejemplo (**Motiv-AWS**). |

## 🚀 El proyecto: "Motiv-AWS"

Una función Lambda en Python que devuelve una mini-web con un saludo personalizado +
una frase motivacional. **No usa librerías externas**, así que se pega directo en la
consola de AWS y entra en la capa gratuita (Always Free).

### Probarlo en tu computadora

```bash
cd proyecto
python test_local.py
# abre el archivo salida.html en tu navegador
```

### Subirlo a AWS

Sigue **[`Guia-Paso-a-Paso.md`](./Guia-Paso-a-Paso.md)**. En resumen:
crear función → pegar el código → Deploy → activar **Function URL** → ¡abrir el link!

## 💰 ¿Por qué es gratis?

AWS Lambda incluye una capa **"Always Free"** que no expira: **1 millón de
ejecuciones** + 400.000 GB-segundos de cómputo cada mes. Esta demo usa una fracción
mínima, así que el costo es **$0**.

---

Hecho con 💜 para que más personas pierdan el miedo a la nube.
