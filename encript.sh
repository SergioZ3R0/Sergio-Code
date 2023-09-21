#!/bin/bash
read -p "Escribe el numero 5 si quieres inverso " reverse
echo -e "Este script necesita dos parametros origen y destino "
read -p "Indica la ruta al archivo origen " archivoOrigen
read -p "Indica la ruta al archivo destino " archivoDestino
while true ; do
        cat $archivoOrigen | tr 'a-zA-Z' 'n-za-mN-ZA-M'>> $archivoDestino
        base64 $archivoDestino
# xxd $archivoDestino
        #tar -cvf compressed $archivoDestino
# if [ echo $? == 0 ]; do
        exit 1
        if [ $reverse == 5 ]; then
                #tar -xvf $qrchivoDestino $archivoOrigen
                #xxd -d archivo
                base64 -d $archivoOrigen
                cat $archivoOrigen | tr 'n-za-mN-ZA-M' 'a-zA-Z'>>$archivoDestino
	fi
done
