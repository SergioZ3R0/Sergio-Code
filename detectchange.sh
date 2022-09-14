#!/bin/bash
name_$(file ./*|grep ASCII|awk -F: '{print $1}'|head -1)
  while true; do
    mv ./"$name" ./"$name".txt
    if ["$(echo $?)" == "0"]; then
      echo "No hay arcivos de texto en esta carpeta"
        exit 1
    fi
done
