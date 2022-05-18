#!/bin/bash
# Este script se utiliza para crear un usuario en su unidad organizativa correspondiente y lo añade a su grupo correspondiente.
#Uso: ./crear_usuari.sh

#Crear usuario
OLDIFS=$IFS
IFS=","
 
while read name OU surname gvname group 
do
echo ""sudo samba-tool user create "${name}" '@ITB2021.' --userou="OU=${OU}"   --surname="${surname}" --given-name="${gvname}"
sudo samba-tool user create "${name}" '@ITB2021.' --userou="OU=${OU}"   --surname="${surname}" --given-name="${gvname}"
#Añadir usuario al grupo correspondiente
sudo samba-tool group addmembers "${group}" "${name}"
done < usuaris.csv
