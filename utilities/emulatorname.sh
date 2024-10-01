 #!/bin/bash
 2 read -p "Dime el nombre del emulador: " origen
 3 read -p "Dime el NUEVO nombre del emulador: " destino
 4 ruta=~/.android/adv/$origen.adv
 5 #find / -name $origen.ini 2>/dev/null and find / -name $origen.adv 2>/dev/nu>
 6
 7 if [ $? -eq 0 ]; then
 8         mv $origen.adv $destino.adv
 9         mv $origen.ini $ruta/$destino.ini
10         sed -i 's/'$origen'/'$destino'/g' $destino.ini
11         exit 1
12 else
13         echo "el emulador no existe"
14 fi
