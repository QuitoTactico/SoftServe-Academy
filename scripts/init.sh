#!/bin/bash

# Cambia al directorio del script
cd "$(dirname "$0")"

# Espera a que la base de datos esté lista antes de aplicar migraciones y cargar datos
echo " "

echo "==================================================="

echo "Esperando a que la base de datos esté disponible..."

# Reintenta la conexión hasta que MySQL esté disponible
until nc -z -v -w30 db 3306
do
  echo "Esperando a MySQL en el host db y puerto 3306..."
  sleep 5
done

echo "MySQL está listo."

# Verifica si el archivo data.json no existe ya en el contenedor para evitar múltiples cargas
if [ ! -f "data.json" ]; then
  echo "Generando data.json desde la base de datos SQLite."
  # Genera el archivo data.json usando settings.py (configurado con SQLite)
  python ../manage.py dumpdata --settings=SoftServeAcademy.settings > data.json
  echo "Archivo data.json generado con éxito desde SQLite."
else
  echo "Archivo data.json ya existe, omitiendo generación."
fi

# Cambia a settings_deployment (con MySQL) y ejecuta las migraciones
echo "Aplicando migraciones en la base de datos MySQL..."
python ../manage.py migrate --settings=SoftServeAcademy.settings_deployment
echo "Migraciones aplicadas con éxito."

# Carga los datos en MySQL solo si la tabla de usuarios no existe
if ! python ../manage.py inspectdb --settings=SoftServeAcademy.settings_deployment | grep -q "auth_user"; then
  echo "Base de datos vacía, cargando datos desde data.json."
  python ../manage.py loaddata data.json --settings=SoftServeAcademy.settings_deployment
  echo "Datos cargados con éxito desde data.json."
else
  echo "Base de datos ya inicializada, no se cargan datos."
fi

# Elimina el archivo data.json si fue cargado
if [ -f "data.json" ]; then
  rm data.json
  echo "Archivo data.json eliminado del contenedor."
fi

# Inicia el servidor de Django usando settings_deployment (con MySQL)
echo "Iniciando el servidor de Django..."
exec python ../manage.py runserver 0.0.0.0:80 --settings=SoftServeAcademy.settings_deployment