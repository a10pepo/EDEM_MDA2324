#No consigo crear con el comando touch, desde consola el los archivos ChuckCasa.sh ni .py,
#Las carpetas sin problema.

#!/bin/bash

rm -r ChuckNorrisCasa

cd / #saldría al directorio raiz
cd ~/ #Entraría al directorio user

mkdir ChuckNorrisCasa
mkdir ChuckNorrisCasa/Results
touch ChuckNorrisCasa/Results ChuckCasa.sh 
touch touch ChuckNorrisCasa/Results ChuckCasa.py
touch ChuckNorrisCasa/Results ChuckCasa.txt

import #Importamos las librerías aquí???
python3 ChuckCasa.py
