FROM python:3.12

# Nombre del directorio del q parte el contenedor
WORKDIR /web-server
# Copia desde Local al Contenedor: COPY [Local] [Contenedor]
COPY requirements.txt /web-server/requirements.txt

# Evita q se suban carpetas cache y actualiza el gestor de paquetes PIP cuando esté disponible
RUN pip install --no-cache-dir --upgrade -r /web-server/requirements.txt
#copia el contenido local a la ubicación del contenedor
COPY . /web-server

# Esto mantiene encendido para conectarse y poder ejecutar scripts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# ----Commands Docker-------
# docker-compose build  -->  para construir el contenedor