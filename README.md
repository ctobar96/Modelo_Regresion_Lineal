# Despliegue de un modelo de Machine Learning como API
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

## Ejecutar el jupyter


## Implementación de la API en FastAPI 