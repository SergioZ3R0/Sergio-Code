 #!/bin/bash
 read -p "Dime el nombre del emulador: " origen
 read -p "Dime el NUEVO nombre del emulador: " destino
 ruta=~/.android/adv
 
 
 find / -name $origen.ini 2>/dev/null || find / -name $origen.adv 2>/dev/nu>
 if [ $? -eq 0 ]; then
         mv $ruta/$origen.adv $ruta/$destino.adv
         mv $ruta/$origen.ini $ruta/$destino.ini
         sed -i 's/'$origen'/'$destino'/g' $destino.ini
         exit 1
 else
         echo "el emulador no existe"
 fi
