#!/bin/bash
# Author: SergioZ3R0
# Script que crea una unidad organitzativa en el dominio de SambaAD autilizando el comando samba-tool
# Uso: ./crear_OU.sh
echo Este scrip se utiliza para crear unidades organizativas mediente samba-tool
# Obtener los paràmetres para la ejecucion del script
read -p "Itroduce el nombre de la unidad organizativa: " Name
read -p "Introduce la descripcion de la unidad organizativa: " Description
# Crear la unitat organitzativa
sudo samba-tool ou create "OU=$Name,DC=error404,DC=local"  --description="$Description"
# Fi scrip

