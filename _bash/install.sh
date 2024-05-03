#!/bin/bash

chmod +x build.sh
chmod +x docker.sh
chmod +x git.sh
chmod +x migrate_db.sh
chmod +x schedular.sh
chmod +x seed.sh

cd ..
chmod +x run.sh

python3 -m venv .venv2
source .venv2/bin/activate

pip install --upgrade pip

pip install -r requirements.txt