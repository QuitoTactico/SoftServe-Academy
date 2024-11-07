#!/bin/bash

# Espera a que la base de datos esté lista antes de aplicar migraciones y cargar datos
echo "Esperando a que la base de datos esté disponible..."

# Reintenta la conexión hasta que MySQL esté disponible
until nc -z -v -w30 db 3306
do
  echo "Esperando a MySQL en el host db y puerto 3306..."
  sleep 5
done

echo "MySQL está listo. Generando data.json y aplicando migraciones."

# Genera el archivo data.json de la base de datos SQLite
python manage.py dumpdata > /app/scripts/data.json

# Ejecuta las migraciones en la base de datos MySQL
python manage.py migrate

# Carga los datos desde el archivo JSON recién generado
python manage.py loaddata /app/scripts/data.json

# Elimina el archivo data.json para que no permanezca en el contenedor
rm /app/scripts/data.json

# Inicia el servidor de Django
exec python manage.py runserver 0.0.0.0:80
