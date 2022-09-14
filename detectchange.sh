#!/bin/bash
name=$(file ./*|grep ASCII|awk -F: '{print $1}'|head -1)
  while true; do
    mv ./"$name" ./"$name".txt
    if ["$(echo $?)" == "0"]; then
      echo "El archivo se ha modificado con exito"
    else
      echo "No hay arcivos de texto en esta carpeta o ya han sido modificados"
        exit 1
    fi
done
