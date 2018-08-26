# ERP module

## Dev Server Setup

install virtualenv

`pip install virtualenv`

clone project to workspace

`git clone https://github.com/dasosjt/erp.git`

get into erp folder

`cd erp`

create virtualenv named erp_env

`virtualenv -p python3 erp_env`

## Install Dev Server Requirements

give executable permission

`chmod +x install-requirements.sh`

install server dev if requirements list is already updated

`./install-requirements.sh`

you must install trough this command after updating requirements.txt

or install directly acquiring virtualenv enviroment with

`source erp_env/bin/activate`

and installing with normal command with pip

`pip install <package_name>`

updating requirements file with pip freeze

`pip freeze > requirements.txt`

## Run Dev Server

give executable permission

`chmod +x run-server.sh`

run install server requirements

`./run-server.sh`