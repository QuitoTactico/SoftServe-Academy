# Usa la imagen completa de Python 3.13
FROM python:3.13

# Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# Instala netcat
RUN apt-get update && apt-get install -y netcat

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copia todo el proyecto a /app
COPY . .

# Copia los scripts y cambia el archivo de settings
COPY scripts /app/scripts
RUN chmod +x /app/scripts/init.sh
RUN mv /app/SoftServeAcademy/settings_deployment.py /app/SoftServeAcademy/settings.py

# Configura variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Expone el puerto 80
EXPOSE 80

# Ejecuta el script de inicialización
CMD ["sh", "/app/scripts/init.sh"]
