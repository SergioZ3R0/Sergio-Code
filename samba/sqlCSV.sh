#!/bin/bash
# Configuración de la base de datos
DB_USER="root"
DB_PASSWORD="SergioZ3R0"
DB_NAME="mi_db"

# Consulta SQL para obtener datos
SQL_QUERY="SELECT * FROM tabla_usuarios;"

result=$(mysql -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e "$SQL_QUERY" 2>/dev/null)
echo $result | cut -d " " -f7- | sed 's/ /,/g;'> usuarios.csv

OLDIFS=$IFS
IFS=","

while read name passwd OU surname gvname group
do
echo "sudo samba-tool user create "${name}" "${passwd}" --userou="OU=${OU}"   --surname="${surname}" --given-name="${gvname}""
sudo samba-tool user create "${name}" "${passwd}" --userou="OU=${OU}"   --surname="${surname}" --given-name="${gvname}"
#Añadir usuario al grupo correspondiente
sudo samba-tool group addmembers "${group}" "${name}"
done < usuarios.csv
