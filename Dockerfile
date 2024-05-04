FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6 -y

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Otorgar permisos de lectura y escritura a todos los archivos y directorios dentro de /app para que cuando se construyan los videos se puedan guardar
RUN chmod -R 777 /app

# Iniciar la aplicación
CMD ["python", "api.py"]