#!/bin/sh
# scripts to run django with gunicorn

set -e

ls -la /vol/
ls -la /vol/web

whoami

python manage.py collectstatic --noinput
python manage.py migrate

gunicorn --bind :8000 --workers 2 homey.wsgi