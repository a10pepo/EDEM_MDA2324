#!/bin/bash

echo "Eliminando el directorio 'master' si existe para limpiar la ejecución anterior..."
rm -r ~/master

echo "Cambio al directorio personal"
cd ~

echo "Creo el directorio 'master'"
mkdir ~/master

echo "Me introduzco en el directorio 'master' para trabajar desde ahi"
cd ~/master

echo "Creo los directorios 'linux', 'git' y 'notebook'"
mkdir linux
mkdir git
mkdir notebook

echo "Accedo al directorio 'linux'"
cd ~/master/linux

echo "Creo el archivo 'fichero.sh' en 'linux'..."
touch fichero.sh

echo "Me muevo al directorio 'git', dentro de 'master'"
cd ~/master/git

echo "Creo el archivo 'fichero2.txt' en 'git'"
touch fichero2.txt

echo "Voy al directorio 'notebook' dentro de 'master'"
cd ~/master/notebook

echo "Creo los directorios 'jupiter' y 'colab' en 'notebook'"
mkdir jupiter
mkdir colab

echo "Me meto en el directorio 'jupiter'"
cd ~/master/notebook/jupiter
echo "Creo el archivo 'f3.txt' dentro de 'jupiter'"
touch f3.txt

echo "Me meto al directorio 'colab'"
cd ~/master/notebook/colab
echo "Creo el archivo 'f4.txt' en 'colab'"
touch f4.txt

echo "Tarea completada"
