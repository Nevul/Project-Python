#!/bin/bash
FROM python:3.11

# Nombre del directorio del q parte el contenedor
WORKDIR /App
# Copia desde Local al Contenedor: COPY [Local] [Contenedor]
COPY requirements.txt /App/requirements.txt

# Evita q se suban carpetas cache y actualiza el gestor de paquetes PIP cuando esté disponible
RUN pip install --no-cache-dir --upgrade -r /App/requirements.txt
#copia el contenido local a la ubicación del contenedor
COPY . /App

CMD bash -c "while true; do sleep 1; done"

# ----Commands Docker-------
# docker-compose build  -->  para construir el contenedor