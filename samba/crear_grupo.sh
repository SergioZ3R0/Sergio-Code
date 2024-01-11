#!/bin/bash
#Author: SergioZ3R0
# Script que crea un grupo dentro de una unidad organitzativa en  el dominio de SambaAD utilizando el comando samba-tool
# Ús: ./crear_grup.sh

# Obtener los paràmetres para la ejecucion del script (grupo, unidad organitzativa i descripción)
read -p "Introduce el nombre del grupo: " GName
read -p "Introduce el nombre de la OU a la que estara asociado: " OUName
read -p "Introduce la descripcion del grupo: " Description
# Crear el grup
sudo samba-tool group add "$GName" --groupou="OU=$OUName" --description="$Description"
# Fi script
