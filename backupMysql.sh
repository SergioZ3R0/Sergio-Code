#!/bin/bash
# Author: SergioZ3R0
# Configuración de la base de datos
DB_NAME="TEST"
DB_USER="root"
DB_PASS="pirineus"

# Directorio de destino para la copia de seguridad
BACKUP_DIR="$HOME"

# Nombre del archivo de copia de seguridad (incluyendo la fecha actual)
BACKUP_FILE="$BACKUP_DIR/db_backup_$(date +'%Y%m%d_%H%M%S').sql"

# Comando para hacer la copia de seguridad de la base de datos
mysqldump -u"$DB_USER" -p"$DB_PASS" "$DB_NAME" > "$BACKUP_FILE"

# Verificar si la copia de seguridad se ha realizado con éxito
if [ $? -eq 0 ]; then
    echo "Copia de seguridad de la base de datos \"$DB_NAME\" realizada con éxito en: $BACKUP_FILE"
else
    echo "Error al realizar la copia de seguridad de la base de datos \"$DB_NAME\""
fi
