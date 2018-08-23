#!/usr/bin/env bash

#run in erp folder
#erp_env is virtualenv folder

source erp_env/bin/activate

export FLASK_APP=erp_app/app.py
export FLASK_ENV=development

python -m flask run