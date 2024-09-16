!#/bin/bash
read -p "tell me the users file" file
OLDIFS=$IFS
IFS=","
 
while read name group secgroup 
do
useradd $1 -m -g $2 -G $3 -s /bin/bash
< $file
