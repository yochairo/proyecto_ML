# Proyecto FastAPI con Poetry

Este proyecto utiliza FastAPI para crear una API web y Poetry para la gestión de dependencias.

## Instalación de Poetry y ejecución de la aplicación de FastAPI

1. Instalar Poetry si no lo tienes. Puedes instalar Poetry utilizando el siguiente comando:
          pip install poetry
2. Una vez que estés en el directorio del proyecto, instala las dependencias utilizando Poetry:
          poetry shell
          poetry install
3. Para ejecutar la aplicación FastAPI con Uvicorn, utiliza el siguiente comando:
          uvicorn main:app --reload --port 8000
   
