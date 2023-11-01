#!/bin/bash
echo ""

echo "Para empezar nos aseguramos de estar en el directorio de conexión con "cd ~" y borramos la carpeta MASTER2 si existe "

cd ~/Desktop
rm -rf MASTER2

echo "Ahora creamos el directorio MASTER"

mkdir MASTER2

echo "nos movemos dentro del directorio y creamos los subdirectorios: NOTEBOOK, LINUX Y GIT. cd ~/MASTER y luego mkdir NOTEBOOK GIT LINUX"

cd ./MASTER2

mkdir NOTEBOOK GIT LINUX

echo "una vez creados generamos los archivos .txt desdeados en cada uno de ellos con touch"

mkdir ./NOTEBOOK COLLAB
mkdir ./NOTEBOOK JUPITER
touch ./GIT file1.txt
touch ./NOTEBOOK/JUPITER notebook1.txt

