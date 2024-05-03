#!/bin/bash

cd ..

msg="settings file updated"

git add .
git commit -m "${msg}"
git push
