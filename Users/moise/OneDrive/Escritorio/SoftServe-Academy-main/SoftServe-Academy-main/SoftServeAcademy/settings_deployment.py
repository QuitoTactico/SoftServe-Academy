from .settings import *  # Importa el resto de la configuración desde settings.py

# Configuración de la base de datos MySQL para despliegue
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "softserve-bd",  # Nombre de la base de datos
        "USER": "admin",  # Usuario de MySQL
        "PASSWORD": "1234",  # Contraseña de MySQL
        "HOST": "db",  # Nombre del servicio de MySQL en Docker Compose
        "PORT": "3306",  # Puerto de MySQL
    }
}
