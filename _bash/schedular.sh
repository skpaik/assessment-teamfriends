#!/bin/bash

cd ..

# celery -A app worker --loglevel=info

celery -A celery_app worker -l info -E