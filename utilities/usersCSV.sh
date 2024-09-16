!#/bin/bash
read -p "tell me the users file" file
OLDIFS=$IFS
IFS=","
 
while read name group secgroup; do
 useradd ${name} -m -g ${group} -G ${secgroup} -s /bin/bash
 if [ (echo $? == 0) ]; then
  echo "Faltan parametros o los parametros no estan en el orden correcto\n Ej: name,group,secgroup"
done < $file

