!#/bin/bash
read -p "tell me the users file" file
OLDIFS=$IFS
IFS=","
 
while read name group secgroup 
do
useradd ${name} -m -g ${group} -G ${secgroup} -s /bin/bash
< $file
