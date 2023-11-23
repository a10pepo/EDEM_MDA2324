**¿Cuáles son los permisos de los directorios presentes en el directorio raíz y en nuestro directorio de usuario? ¿A quién pertenecen los ficheros y qué permisos tienen los distintos usuarios del ordenador?**
localhost:~# cd /
localhost:/# ls -l
localhost:/# ls -l root
**Crea un directorio en tu home y muestra los permisos que tiene.**
localhost:/# mkdir midirectorio
localhost:/# ls -l
**Cambia los permisos para que sólo tu usuario pueda acceder al nuevo directorio.**
localhost:/# chmod 700 midirectorio
**Crea un fichero nuevo y dale permisos de ejecución para todos los usuarios.**
localhost:/# cd midirectorio
localhost:/midirectorio# touch fichero.txt
localhost:/midirectorio# chmod 111 fichero.txt
**Último fichero modificado en el directorio /etc.**
localhost:/# find /etc -type f -mtime 0
**Lista los ficheros de /etc con su tamaño y ordénalos por tamaño.**
localhost:/etc# ls -lS
**Copia todos los ficheros y directorios del directorio /etc cuyo nombre comience por s. ¿Has podido copiarlos todos?**
localhost:/etc# cp -d [s*]*
**¿Cuánto espacio libre queda en las distintas particiones del sistema?**
localhost:/etc# df -h
**¿Cuánto espacio ocupan todos los ficheros y subdirectorios de tu $HOME?**
localhost:/etc# du -ha