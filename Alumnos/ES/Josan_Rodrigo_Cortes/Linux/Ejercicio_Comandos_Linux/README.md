# Linux_Comandos
# Para entregar este ejercicio, debes copiar este archivo en tu carpeta de alumno y completar las respuestas a las preguntas que se formulan en el mismo.
# Una vez completado, debes subirlo a vuestro repositorio remoto de GitHub y realizar una Pull Request poniendo a Pedro Nieto como reviewer.

#!/bin/bash


echo "Ejercicio de comandos en la consola de linux."

  echo "1.Listar todos los archivos del directorio bin."
  ls -a bin

  echo "2.Listar todos los archivos del directorio tmp."
  ls tmp -a
    
  echo "3.Listar todos los archivos del directorio etc que empiecen por t."
  ls -a /etc/t*

  echo "4.Listar todos los archivos del directorio dev que empiecen por tty."
  ls -a /dev/tty*
    
  echo "5.Listar todos los archivos del directorio dev que empiecen por tty y acaben en 3." 
  ls -a tty*3
  # Hay alguno??
  echo "6.Listar todos los archivos del directorio dev que empiecen por t y acaben en C1."
  ls -a /dev/t*c1
  # Hay alguno?
  echo "7.Listar todos los archivos, incluidos los ocultos, del directorio raíz."
  ls -a

  echo "8.Listar todos los archivos del directorio etc que no empiecen por t."
  ls -d /etc/[^t]*
  
  echo "9.Listar todos los archivos del directorio usr y sus subdirectorios."
  ls /usr *

  echo "10.Cambiarse al directorio tmp, crear directorio PRUEBA."
  mkdir /tmp/PRUEBA
    
  echo "11.Verificar que el directorio actual ha cambiado."
  pwd
  
  echo "12.Mostrar el día y la hora actual."
  date

  echo "13.Con un solo comando posicionarse en el directorio $HOME."
  cd /$HOME
 
  echo "14.Verificar que se está en él."
  pwd

  echo "15.Listar todos los ficheros del directorio HOME mostrando sus permisos."
  ls -al $HOME #opcion1
  ls -l $HOME # opcion2

  echo "16.Borrar todos los archivos y directorios visibles de vuestro directorio PRUEBA."
  rmdir /tmp/PRUEBA
    
  echo "17.Crear los directorios dir1, dir2 y dir3 en el directorio PRUEBA. Dentro de dir1 crear el directorio dir11. Dentro del directorio dir3 crear el directorio dir31. Dentro del directorio dir31, crear los directorios dir311 y dir312."
  mkdir /tmp/PRUEBA/dir1
  mkdir /tmp/PRUEBA/dir2 
  mkdir /tmp/PRUEBA/dir3
  mkdir /tmp/PRUEBA/dir1/dir11
  mkdir /tmp/PRUEBA/dir3/dir31
  mkdir /tmp/PRUEBA/dir3/dir31/dir311
  mkdir /tmp/PRUEBA/dir3/dir31/dir312

  echo "18.Copiar el archivo /etc/motd a un archivo llamado mensaje de vuestro directorio PRUEBA."
    
  touch /etc/motd /tmp/PRUEBA/mensaje.txt  

  echo "19.Copiar mensaje en dir1, dir2 y dir3."
  cp mensaje.txt /tmp/PRUEBA/dir1
  cp mensaje.txt /tmp/PRUEBA/dir2
  cp mensaje.txt /tmp/PRUEBA/dir3

  # 20.Comprobar el ejercicio anterior mediante un solo comando.
    

    
   
