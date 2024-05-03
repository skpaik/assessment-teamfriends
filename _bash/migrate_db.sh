#!/bin/bash

cd ..

python3 manage.py makemigrations
python3 manage.py migrate

python3 manage.py syncdb --noinput
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@admin.com', 'admin')" | python manage.py shell

