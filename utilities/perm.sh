#Analisis de archivos potencialmente peligrosos

find / \( -perm -4000 -o -perm 2000 \) -ls 2>/dev/null > files.txt
