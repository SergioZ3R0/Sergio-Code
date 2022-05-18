#!/bin/bash
# Script que crea una unitat organitzativa al domini de SambaAD amb la comanda samba-tool
# Ús: ./crear_OU.sh
echo Este scrip se utiliza para crear unidades organizativas mediente samba-tool
# Obtenir els dos paràmetres per entrada de l'usuari
read -p "Itroduce el nombre de la unidad organizativa: " Name
read -p "Introduce la descripcion de la unidad organizativa: " Description
# Crear la unitat organitzativa
sudo samba-tool ou create "OU=$Name,DC=error404,DC=local"  --description="$Description"
# Fi scrip

