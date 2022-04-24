#!/bin/bash 
source /opt/miniconda3/bin/activate matt1
export FLASK_APP=main
export FLASK_ENV=development
nohup flask run --host=0.0.0.0 > main.log 2>&1 &

