# 🚀 Guía Paso a Paso — Sube tu Primera Lambda (¡GRATIS!)

**Charla:** Hands-on with AWS Lambda
**Por:** Geraldinne Laruta

Esta guía es para hacerla **con tu cuenta personal de AWS**, en vivo, durante la
charla. Al final tendrás una mini-página web funcionando en la nube **sin
servidores** y **sin pagar nada**. Toda la demo se ejecuta dentro de la capa
**"Always Free"** de Lambda.

> ⏱️ Tiempo estimado de la demo en vivo: **25–35 minutos**.

---

## 🎯 Lo que vamos a lograr

1. Crear una función Lambda en Python.
2. Pegar el código del proyecto (`lambda_function.py`).
3. Probarla dentro de AWS.
4. Publicarla con una **Function URL** (un link público).
5. Abrirla en el navegador y verla viva. ✨

---

## 💰 ¿Por qué es gratis?

AWS Lambda tiene una capa **"Always Free"** que **no expira nunca** y aplica a
todas las cuentas: **1 millón de ejecuciones gratis cada mes** + 400,000
GB-segundos de cómputo. Nuestra demo usa muy poquito de eso, así que el costo
real es **$0**.

> 💡 **Bonus:** si creas una cuenta nueva (después de julio 2025), AWS te da
> **$100 en créditos** al registrarte y puedes ganar **$100 más** completando
> tareas. Una de esas tareas es, literalmente, **"crear una función Lambda"**
> (te da $20). ¡Esta demo te puede regalar créditos! 🎁

---

## ✅ Requisitos

- Una cuenta de AWS (abajo te digo cómo crearla).
- Un navegador (Chrome, Firefox, Edge…).
- El archivo `lambda_function.py` de la carpeta `proyecto/` abierto y listo para copiar.

> ⚠️ **Importante:** AWS pide una tarjeta de crédito/débito al registrarte (es
> su política para verificar identidad). Con la capa gratuita **no te van a
> cobrar** por esta demo. Más abajo te muestro cómo poner una alerta de gasto
> para tu tranquilidad.

---

## PARTE 1 — Entrar (o crear) tu cuenta AWS

### Si ya tienes cuenta
Entra a **https://console.aws.amazon.com** e inicia sesión. Salta a la **Parte 2**.

### Si NO tienes cuenta
1. Ve a **https://aws.amazon.com** y haz clic en **"Create an AWS Account"**.
2. Pon tu correo, una contraseña y el nombre de la cuenta.
3. Cuando te pregunte, elige el **"Free account plan"** (Plan gratuito).
4. Completa tus datos y agrega una tarjeta (no se cobra dentro de la capa gratuita).
5. Verifica tu teléfono y termina el registro.
6. Inicia sesión en **https://console.aws.amazon.com**.

---

## PARTE 2 — Crear la función Lambda

1. Arriba, en la barra de búsqueda, escribe **`Lambda`** y haz clic en el servicio **Lambda**.
2. (Opcional pero recomendado) Arriba a la derecha, fíjate en la **región**.
   Elige una cercana, por ejemplo **`us-east-1` (N. Virginia)** o **`sa-east-1` (São Paulo)**.
   Usa siempre la misma región durante toda la demo.
3. Haz clic en el botón naranja **"Create function"**.
4. Deja seleccionado **"Author from scratch"** (Crear desde cero).
5. Llena:
   - **Function name:** `mi-primera-lambda`
   - **Runtime:** `Python 3.13` (o la versión de Python más reciente disponible)
   - **Architecture:** deja **`x86_64`** (la opción por defecto está bien)
6. Haz clic en **"Create function"**. 🎉

> Acabas de crear tu primera función. AWS te dio automáticamente los permisos
> básicos para que funcione. **No tienes que configurar ningún servidor.**

---

## PARTE 3 — Pegar el código del proyecto

1. Baja hasta la sección **"Code"** (Código). Verás un editor con un archivo
   llamado `lambda_function.py`.
2. **Borra todo** lo que hay en ese editor.
3. Abre el archivo `proyecto/lambda_function.py` (el del proyecto), **copia todo**
   y **pégalo** en el editor de AWS.
4. Haz clic en **"Deploy"** (el botón arriba del editor). Verás un mensaje de
   "Changes deployed". ✅

> 🔁 **Regla de oro:** cada vez que cambies el código, haz clic en **Deploy**.
> Si no, AWS sigue usando la versión anterior.

---

## PARTE 4 — Probar la función dentro de AWS

1. Haz clic en la pestaña **"Test"**.
2. Te pedirá crear un evento de prueba:
   - **Event name:** `prueba`
   - En el cuadro de texto (Event JSON), pega esto:
     ```json
     {
       "queryStringParameters": { "nombre": "Geraldinne" }
     }
     ```
3. Haz clic en **"Save"** y luego en **"Test"**.
4. Abajo aparecerá **"Execution result: succeeded"** y un montón de HTML en la
   respuesta. ¡Eso significa que tu código corrió en la nube! ⚡

> 😅 Si sale un error en rojo, revisa la sección **"Solución de problemas"** al final.

---

## PARTE 5 — Publicar con una Function URL (el momento mágico ✨)

Aquí convertimos tu función en una **página web pública**.

1. Ve a la pestaña **"Configuration"** y luego, en el menú de la izquierda,
   haz clic en **"Function URL"**.
2. Haz clic en **"Create function URL"**.
3. En **Auth type**, elige **`NONE`** (para que cualquiera pueda abrir el link
   en la demo).
   > Aparecerá una advertencia de que será público. Para una demo está bien.
   > Para algo real, usarías `AWS_IAM`.
4. Haz clic en **"Save"**.
5. AWS te dará una **URL** parecida a:
   `https://abcd1234.lambda-url.us-east-1.on.aws/`
   **Cópiala.**

### ¡Ábrela!
- Pega la URL en tu navegador y presiona Enter → verás la tarjeta morada. 💜
- Ahora pruébala personalizada agregando tu nombre al final:
  `https://...on.aws/?nombre=Geraldinne`
- 👉 **Truco para la charla:** muestra el link en pantalla (o un QR) y pide a
  los asistentes que la abran en su celular con SU nombre. Cada quien verá su
  saludo. ¡Eso engancha! 🤳

> 🟢 **Tu Lambda queda "corriendo" en esa URL.** No hay servidores prendidos
> gastando dinero: solo se "despierta" cuando alguien entra al link, y se
> "duerme" cuando nadie la usa. Por eso es tan barata.

---

## PARTE 6 — Ver los logs (opcional, pero se ve increíble)

Cada vez que tu función corre, deja un registro.

1. Ve a la pestaña **"Monitor"** → **"View CloudWatch logs"**.
2. Abre el grupo de logs más reciente. Verás líneas con `START`, `END` y
   `REPORT` (incluye cuántos milisegundos tardó y cuánta memoria usó).

> 💡 Esto demuestra el concepto: **solo pagas por los milisegundos que se ejecuta**.

---

## PARTE 7 — ¿Cuánto cuesta? (Spoiler: nada)

- Caímos en la capa **Always Free**: 1,000,000 ejecuciones/mes gratis.
- Una demo con cientos de visitas usa una fracción mínima → **$0**.
- La Function URL **no tiene costo extra**.

### Para tu tranquilidad: pon una alerta de gasto (1 minuto)
1. Busca **"Billing"** o **"AWS Budgets"** en la consola.
2. Crea un **budget** tipo **"Zero spend budget"** (o de $1 USD).
3. Pon tu correo → si algo llegara a generar costo, AWS te avisa al instante.

---

## PARTE 8 — Limpieza (opcional, después de la charla)

Si quieres dejar todo como estaba:

1. (Opcional) En **Configuration → Function URL**, borra la URL.
2. En la lista de funciones, selecciona `mi-primera-lambda` →
   **Actions → Delete**.

> Si la dejas, también está bien: dentro de la capa gratuita no genera costo.

---

## 🆘 Solución de problemas comunes

| Síntoma | Causa probable | Solución |
|---|---|---|
| El navegador descarga un archivo en vez de mostrar la página | Falta el header de tipo de contenido | Confirma que el código tiene `"Content-Type": "text/html; charset=utf-8"` y que hiciste **Deploy** |
| `Internal Server Error` al abrir la URL | Error en el código o no hiciste Deploy | Revisa la pestaña **Test**, lee el mensaje rojo, corrige y **Deploy** |
| La página dice `Region: desconocida` | Estás probando en local (sin AWS) | Es normal en `test_local.py`. En AWS sí mostrará la región |
| No encuentro "Function URL" | Estás en otra pestaña | Ve a **Configuration → Function URL** |
| Cambié el código y no se actualiza | Olvidaste hacer Deploy | Haz clic en **Deploy** |
| `Indentation Error` al pegar | Se mezclaron espacios al copiar | Vuelve a copiar el archivo completo y pégalo de nuevo |

---

## 🎤 Mini-guion para presentar en vivo (para ti, Geraldinne)

1. **Engancha:** "¿Qué pasaría si te digo que en 5 minutos vas a tener una
   página web en internet… sin un solo servidor?"
2. **Crea la función** (Parte 2) mientras explicas: *runtime = el lenguaje*,
   *handler = la puerta de entrada*.
3. **Pega y Deploy** (Parte 3). Recalca la regla de oro del Deploy.
4. **Test** (Parte 4): "miren, ya corrió en la nube de AWS".
5. **Function URL** (Parte 5): este es el clímax. Abre el link en vivo.
6. **Pásalo al público:** comparte el QR/link y que cada quien ponga su nombre.
7. **Logs** (Parte 6): "solo pagué por estos milisegundos".
8. **Cierra:** "esto fue gratis, vive en la nube, y escala solo. Eso es
   serverless." 🎉

---

¡Listo! Si llegaste hasta aquí, ya eres oficialmente **serverless**. 💜⚡
