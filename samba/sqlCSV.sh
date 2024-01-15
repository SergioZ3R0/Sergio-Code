#!/bin/bash
# Author: SergioZ3R0
# Configuración de la base de datos
DB_USER="root"
DB_PASSWORD="SergioZ3R0"
DB_NAME="mi_db"

# Consulta SQL para obtener datos
SQL_QUERY="SELECT * FROM tabla_usuarios;"

result=$(mysql -u "$DB_USER" -p"$DB_PASSWORD" -D "$DB_NAME" -e "$SQL_QUERY" 2>/dev/null)
echo $result | cut -d " " -f7- | sed 's/ /,/g;'> usuarios.csv
sudo sed -i 's/\([^,]*,[^,]*,[^,]*,[^,]*,[^,]*,[^,]*,\)/&\n/g' usuarios.csv
OLDIFS=$IFS
IFS=","
while IFS= read -r line; do
        while read name passwd OU surname gvname group; do
                echo "sudo samba-tool user create "${name}" "${passwd}" --userou="OU=${OU}"   --surname="${surname>
                sudo samba-tool user create "${name}" "${passwd}" --userou="OU=${OU}"   --surname="${surname}" --g>
                #Añadir usuario al grupo correspondiente
                sudo samba-tool group addmembers "${group}" "${name}"
                sed -i '1d' "usuarios.csv"
        done < usuarios.csv
done < usuarios.csv
