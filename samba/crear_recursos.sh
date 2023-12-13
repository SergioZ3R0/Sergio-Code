#!/bin/bash
#Author: SergioZ3R0
#Este script se utiliza para crear recuros, asignarle los permisos y sus propietarios.
#Uso: ./crear_recursos.sh "recurso" "propietario" "permisos"
if [ $# -ne 4 ]
then
	echo se necesita 4 argumentos para poder ejecutar el script: recurso, propietario, grupo y permisos
	exit
fi
#Crear el recurso
mkdir /var/error404/$1
#Asignarle el porpietario
chown "$2:$3" /var/error404/$1
#Asignarle los permisos
chmod "$4" /var/error404/$1
#final
