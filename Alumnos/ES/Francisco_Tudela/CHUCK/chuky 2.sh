#!/bin/bash
echo "Creando directorio results..."
mkdir -p chuck/results
touch chuck/results/results.txt
pip install requests
python3 CHUCKY.py
