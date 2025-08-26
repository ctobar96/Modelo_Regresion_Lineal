# Despliegue de un modelo de Machine Learning como API
**URL pública: https://modelo-regresion-lineal.onrender.com**


En esta tarea deberás tomar uno de los modelos de Machine Learning que hayas desarrollado durante el programa de magíster y convertirlo en un producto de datos funcional, accesible mediante una API construida con FastAPI y desplegada en Render, siguiendo las buenas prácticas vistas en clases.

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


## Despliegue de la API en Render

### Pasos para desplegar
1. Añadir un archivo requirements.txt actualizado.

2. En el dashboard de Render, crear un Web Service apuntando al repositorio.

3. Configurar:

- Build Command: pip install -r requirements.txt

- 4. Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Render reconstruye e inicia automáticamente la API.


## Pruebas desde un Cliente Externo (30 puntos)
Se incluye client.ipynb (o client.py) que realiza tres peticiones distintas y muestra datos enviados y respuestas.