#!/bin/bash
echo "Hello world"
mkdir CHUCKO
mkdir ./CHUCKO/Results
touch ./CHUCKO/Results/chucky.txt
pip3 install requests
pip3 install time
python3 ChuckAPI.py