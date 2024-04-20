#!/bin/bash
# for assignment
# check if python3 is available
# check if venv exists

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
python3 main.py

#for another bash file can add

#chmod +x another.sh
# ./another.sh