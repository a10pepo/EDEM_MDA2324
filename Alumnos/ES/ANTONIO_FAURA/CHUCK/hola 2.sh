#!/bin/bash
echo "Hola Mundo"
cd ~
mkdir -p /CHUCK
mkdir -p ~/CHUCK/RESULTS
pip install requests
pip install time
python3 chuck.py
#./nombre_script para ejecutar
