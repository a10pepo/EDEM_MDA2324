#Deber **Linux**

Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo. Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.

Ejercicio de comandos en la consola de linux.

<strong>1.Listar todos los archivos del directorio bin</strong>
ls /bin

<strong>2.Listar todos los archivos del directorio tmp</strong>
ls /tmp

<strong>3.Listar todos los archivos del directorio etc que empiecen por t</strong>
ls /etc/t*

<strong>4.Listar todos los archivos del directorio dev que empiecen por tty</strong>
ls /dev/tty*

<strong>5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3</strong>
ls /dev/tty*3

<strong>6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1</strong>
ls /dev/t*C1

<strong>7.Listar todos los archivos, incluidos los ocultos, del directorio raíz</strong>
ls -a /

<strong>8.Listar todos los archivos del directorio etc que no empiecen por t</strong>
ls -d /etc/[^t]*

<strong>9.Listar todos los archivos del directorio usr y sus subdirectorios</strong>
ls -R /usr

<strong>10.Cambiarse al directorio tmp, crear directorio PRUEBA</strong>
cd /tmp
mkdir PRUEBA

<strong>11.Verificar que el directorio actual ha cambiado</strong>
pwd

<strong>12.Mostrar el día y la hora actual</strong>
date

<strong>13.Con un solo comando posicionarse en el directorio $HOME</strong>
cd /HOME

<strong>14.Verificar que se está en él</strong>
pwd

<strong>15.Listar todos los ficheros del directorio HOME mostrando sus permisos</strong>
ls -l

<strong>16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA</strong>
rm -rf /tmp/PRUEBA*

<strong>17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312</strong>
mkdir /tmp/PRUEBA
mkdir /tmp/PRUEBA/dir1 dir2 dir3
mkdir /tmp/PRUEBA/dir1/dir11 
mkdir /tmp/PRUEBA/dir3/dir31    
mkdir /tmp/PRUEBA/dir3/dir31/dir311   
mkdir /tmp/PRUEBA/dir3/dir31/dir312      

<strong>18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA</strong>
cp /etc/motd /tmp/PRUEBA/mensaje

<strong>19.Copiar mensaje en dir1, dir2 y dir3</strong>
cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir1
cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir2
cp /tmp/PRUEBA/mensaje /tmp/PRUEBA/dir3

<strong>20.Comprobar el ejercicio anterior mediante un solo comando</strong>
ls -R /tmp/PRUEBA/dir1 /tmp/PRUEBA/dir2 /tmp/PRUEBA/dir3