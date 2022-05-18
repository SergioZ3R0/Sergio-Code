#!/bin/bash
# Este script se utiliza para crar un usuario en su unidad organizativa correspondiente y lo añade a su grupo correspondiente.
#Uso: ./crear_usuari.sh

#Crear usuario
if [ $# -ne 5 ]
then
	echo Se necesitan 5 argumentos para poder ejecutar el Script
	exit
fi
sudo samba-tool user create "$1" '@ITB2021.' --userou="OU=$2"   --surname="$3" --given-name="$4"
#Añadir usuario al grupo correspondiente
sudo samba-tool group addmembers "$5" $1
