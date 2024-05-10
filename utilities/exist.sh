#!/bin/bash
# Author: SergioZ3R0
read -p "dime un nombre:" nombre
file=comprobar.txt
find -type f -name $nombre 2>/dev/null 1>comprobar.txt
cat comprobar.txt
if [ "$(wc -l "$file" | awk '{print $1}')" == "0" ]; then
        echo -ne "el archivo no existe"
        rm comprobar.txt
else
        echo -ne "El archivo existe"
fi

