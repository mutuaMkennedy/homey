#!/bin/sh
# scripts to run django with gunicorn

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py migrate
python manage.py collectstatic --noinput
gunicorn homey.wsgi:application --bind 0.0.0.0:8000 --workers 2 
