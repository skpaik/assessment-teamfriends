#!/bin/bash

chmod +x run.sh
chmod +x build.sh
chmod +x migrate_db.sh
chmod +x git.sh

source .venv/bin/activate
python3 -m pip install --upgrade pip
python3 -m pip install django
