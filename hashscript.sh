#!/bin/bash
echo -e "Para que este script funcione previamente tienes que haber intalado HASHCAT sudo apt install hashcat\n"
read -p "Introduce el archivo de Output " Output
read -p "Introduce el archivo de Hash " HashFile
read -p "Introduce el archivo de Wordlist " Wordlist
hashnum=1
hashtypes="0 1 2 ... 10000"
while [ "$(wc -l "$HashFile" | awk '{print $1}')" != "0" ]; do
        while read -r Hash; do
                echo -e "\n\e[1;4mCracking\e[1;4;0m:\n$Hash"
                for x in {0..10000}; do
                        rm -rf /home/kali/.local/share/hashcat;
                        hashcat -m $x -a 0 -o $Output $Hash $Wordlist  1>/dev/null 2>/dev/null;
                        if [ "$(echo $?)" == "0" ]; then
                                echo -e "\e[96;1mHASH $hashnum CRACKED\e[1;0m"
                                hashnum=$((hashnum + 1))
                                echo "Module used $x"
                                echo "------------------------------------------------------------------------------------"
                                sed -i '1d' "$HashFile"
                                continue 2
                        elif [ "$x" == "10000" ] && [ "(echo $?)" != "0" ]; then
                                echo -e "\e[91;1mHash $hashnum was imposible to Crack\e[1;0m"
                                touch UnCracked.txt
                                echo -ne "$Hash" >> UnCracked.txt
                                echo "------------------------------------------------------------------------------------"
                                sed -i '1d' "$HashFile"
                                hashnum=$((hashnum + 1))
                                continue 2
                        fi
                done
        done< "$HashFile"
done
