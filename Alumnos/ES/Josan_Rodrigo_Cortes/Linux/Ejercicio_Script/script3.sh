#!/bin/bash

rm -r master

echo "Creación directorio Master"
mkdir master #creo carpeta master
echo "Creación del subdirectorio Linux"
mkdir master/linux #creo carpeta linux
touch master/linux/fichero1.txt #creo fichero dentro de linux
echo "Creación del directorio gift"
mkdir master/git #creo git
touch master/git/fichero2.txt #creo fichero 2 dentro de git
echo "Creación del subdirectorio Notebook"
mkdir master/notebook #creo notebook
echo "Creación del subdirecorio jupyter de notebook"
mkdir master/notebook/jupyter
touch master/notebook/jupyter/f3.txt
echo "Creación del subdirectorio colab de notebook"
mkdir master/notebook/colab
touch master/notebook/colab/f4.txt

echo overflow revisar

