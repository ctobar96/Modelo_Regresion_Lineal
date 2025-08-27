# API de Predicción de Precio de Casas con Modelo de Regresión Lineal
**URL pública: https://modelo-regresion-lineal.onrender.com**

Esta API permite predecir el precio de una casa en función de varias características utilizando un modelo de regresión lineal desplegado con FastAPI.

## Objetivo
Lograr empaquetar un modelo como un servicio de predicción accesible a través de la web, incluyendo pruebas automatizadas desde un cliente y documentación que permita a un tercero realizar consultas sin fricción.


## Pasos previos utilizando uv
### Prerrequisito: Tener uv instalado en tu computadora.
uves una herramienta moderna y rápida para gestionar entornos virtuales y dependencias de Python. Como alternativa a la conversación, puedes usar uvque ofrece un rendimiento significativamente mejor.

### 1. Instalación de uv
Si no tienes uv instalado, puedes instalarlo con:
En Windows (usando pip):
```shell
pip install uv
```

### 2. Creando el entorno virtual (Virtual Environment)
Abre tu terminal y sitúate en la carpeta raíz de tu proyecto.
Ejecuta el comando: 
```shell
uv venv

```
Esto generará un directorio oculto  `.venv` que contendrá el intérprete de Python aislado y las librerías instaladas.

### 3. Activando el entorno virtual

```shell
.venv\Scripts\activate
```

### 4. Instalando las dependencias con uv
Con el entorno activado, instala todas las dependencias directamente desde requirements.txt:
```shell
uv pip install -r requirements.txt
```


## Archivos principales
- main.py: arranque de la aplicación, carga del modelo y definición de rutas.

- client.ipynb: Prueba con datos de ejemplo.

- model/linearRegression.joblib: modelo previamente entrenado serializado con Joblib.

- requirements.txt: lista de dependencias necesarias.

- render.yaml: Archivo de configuración para Render (esto ayuda a que el deploy se haga bien). 


## Despliegue de la API en Render

### Pasos para desplegar
1. Añadir un archivo requirements.txt actualizado.

2. En el dashboard de Render, crear un Web Service apuntando al repositorio.

3. Configurar:

- Build Command: pip install -r requirements.txt

- 4. Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Render reconstruye e inicia automáticamente la API.


---

## Estructura del JSON de entrada

Se espera un JSON con los siguientes campos:

| Campo            | Tipo    | Descripción                                   | Valores permitidos       |
|------------------|---------|-----------------------------------------------|-------------------------|
| `area`           | entero  | Área de la casa en pies cuadrados              | Número positivo          |
| `bedrooms`       | entero  | Número de habitaciones                          | Número entero >= 0       |
| `bathrooms`      | entero  | Número de baños                                | Número entero >= 0       |
| `stories`        | entero  | Número de pisos (niveles)                      | Número entero >= 0       |
| `guestroom`      | entero  | Indica si tiene cuarto de huéspedes            | 0 = Sí, 1 = No          |
| `hotwaterheating`| entero  | Indica si tiene calentador de agua              | 0 = Sí, 1 = No          |
| `airconditioning`| entero  | Indica si tiene aire acondicionado             | 0 = Sí, 1 = No          |
| `parking`        | entero  | Número de lugares de estacionamiento           | Número entero >= 0       |

---

## Ejemplo de consulta válida

```json
{
  "area": 8502,
  "bedrooms": 5,
  "bathrooms": 2,
  "stories": 2,
  "guestroom": 0,
  "hotwaterheating": 1,
  "airconditioning": 0,
  "parking": 2
}
```

### Cómo hacer una consulta POST

- URL del endpoint: https://modelo-regresion-lineal.onrender.com/docs

- Buscar el endpoint /predict_price

- Hacer clic en "Try it out"

- Ingresar el JSON en el cuadro que aparece

- Ejecutar la petición y ver la respuesta en la misma página.

**Respuesta esperada**, la API devolverá un JSON con el precio predicho
