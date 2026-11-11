# Imagen única para los tres servicios. La versión de Python se recibe
# como argumento de construcción desde compose.yml (3.11, 3.12 o 3.13).
ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-slim

# Entorno virtual en /opt/venv: queda fuera de /app, que compose.yml
# sustituye por la carpeta del proyecto. Anteponer su bin/ al PATH
# equivale a dejarlo activado para todas las órdenes siguientes.
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /app

# Primero sólo las dependencias: Docker reutiliza esta capa mientras
# requirements.txt no cambie, aunque cambie el código.
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Después el código (en desarrollo, el volumen lo reemplaza).
COPY . .

# Sin escritorio, Flet se sirve como aplicación web en este puerto.
ENV FLET_FORCE_WEB_SERVER=true
ENV FLET_SERVER_PORT=8550

CMD ["python", "src/app.py"]
