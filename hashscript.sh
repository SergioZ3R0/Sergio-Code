#!/bin/bash
echo "Para que este script funcione previamente tienes que haber intalado HASHCAT sudo apt install hashcat"
read -p "Introduce el archivo de Output " Output
read -p "Introduce el archivo de Hash " Hash
read -p "Introduce el archivo de Wordlist " Wordlist
hashtypes="0 1 2 ... 10000"
hashCount=$(wc -l "$Hash" | awk '{print $1}')
while [ "$hashCount">="1" ]; do
        for x in {0..10000}; do
                rm -rf /home/kali/.local/share/hashcat
                hashcat --remove -m $x -a 0 -o $Output $Hash $Wordlist  1>/dev/null 2>/dev/null;
                if [ "$(echo $?)" == "0" ]; then
                        echo "HASH CRACKED"
                        exit 5
                fi
        done
done
