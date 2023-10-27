## Ejercicios 
# 1.Listar todos los archivos del directorio bin.
cd /bin
ls /bin
# 2.Listar todos los archivos del directorio tmp.
cd /tmp
ls /tmp
# 3.Listar todos los archivos del directorio etc que empiecen por t
cd /etc
ls /etc/t*
# 4.Listar todos los archivos del directorio dev que empiecen por tty.
ls /dev/tty*
# 5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3.
ls /dev/tty*3
# 6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1.
ls /dev/t*C1
# 7.Listar todos los archivos, incluidos los ocultos, del directorio raíz.
ls /
ls -al
# 8.Listar todos los archivos del directorio etc que no empiecen por t.
ls /etc/
# 9.Listar todos los archivos del directorio usr y sus subdirectorios.
ls /usr
# 10.Cambiarse al directorio tmp, crear directorio PRUEBA.
mkdir tmp/PRUEBA
# 11.Verificar que el directorio actual ha cambiado.
pwd
# 12.Mostrar el día y la hora actual.
date
# 13.Con un solo comando posicionarse en el directorio $HOME.
cd /home
# 14.Verificar que se está en él.
pwd
# 15.Listar todos los ficheros del directorio HOME mostrando sus permisos.
chmod
# 16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA.
rm -rf /PRUEBA
# 17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312.
mkdir PRUEBA/dir1 PRUEBA/dir2 PRUEBA/dir3
mkdir PRUEBA/dir1/dir11 PRUEBA/dir3/dir31
mkdir PRUEBA/dir3/dir31/dir311 PRUEBA/dir3/dir31/dir312
# 18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA.
touch motd
# 19.Copiar mensaje en dir1, dir2 y dir3.
cp tmp/PRUEBA/mensaje tmp/PRUEBAdir1
cp tmp/PRUEBA/mensaje tmp/PRUEBAdir2 
cp tmp/PRUEBA/mensaje tmp/PRUEBAdir3
# 20.Comprobar el ejercicio anterior mediante un solo comando.
cd /tmp/PRUEBA/dir1
