#!/bin/bash

cd /users/andresrsalamanca
echo "a continuacion se creara el directorio en: $PWD"
mkdir -p master/linux
echo "se ha creado directorio master en users/andresrsalamanca"
mkdir master/git
echo "se ha creado carpeta git dentro de directorio master"
mkdir master/notebook
echo "se ha creado carpeta notebook dentro de directorio master"
cd master/notebook
mkdir jupiter collab
echo "se ha creado carpetas jupiter y collab dentro de carpeta notebook"
mkdir -p jupiter collab && touch jupiter/fichero3.txt && touch collab/fichero4.txt
echo "En la carpeta jupiter se ha creado fichero3.txt y en la carpeta collab el fichero4.txt"

