#!/bin/bash
line=1
name=$(file ./*|grep ASCII|awk -F: '{print $"line"}'|head -1)
  while true; do
    mv ./"$name" ./"$name".txt
    if ["$(echo $?)" == "0"]; then
      echo "El archivo se ha modificado con exito"
      line = $line+1
    else
      echo "No hay arcivos de texto en esta carpeta o ya han sido modificados"
        line = $line+1
        exit 1
    fi
done
