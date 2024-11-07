#!/bin/bash

# Espera a que la base de datos esté lista antes de aplicar migraciones y cargar datos
echo "Esperando a que la base de datos esté disponible..."

# Reintenta la conexión hasta que MySQL esté disponible
until nc -z -v -w30 db 3306
do
  echo "Esperando a MySQL en el host db y puerto 3306..."
  sleep 5
done

echo "MySQL está listo. Generando data.json desde la base de datos SQLite."

# Genera el archivo data.json usando settings.py (que está configurado con SQLite)
python manage.py dumpdata --settings=SoftServeAcademy.settings > /app/scripts/data.json
echo "Archivo data.json generado con éxito desde SQLite."

# Cambia a settings_deployment (con MySQL) y ejecuta las migraciones
echo "Aplicando migraciones en la base de datos MySQL..."
python manage.py migrate --settings=SoftServeAcademy.settings_deployment
echo "Migraciones aplicadas con éxito."

# Carga los datos desde el archivo JSON recién generado en MySQL
echo "Cargando datos desde data.json en la base de datos MySQL..."
python manage.py loaddata /app/scripts/data.json --settings=SoftServeAcademy.settings_deployment
echo "Datos cargados con éxito desde data.json."

# Elimina el archivo data.json para que no permanezca en el contenedor
rm /app/scripts/data.json
echo "Archivo data.json eliminado del contenedor."

# Inicia el servidor de Django usando settings_deployment (con MySQL)
echo "Iniciando el servidor de Django..."
exec python manage.py runserver 0.0.0.0:80 --settings=SoftServeAcademy.settings_deployment
