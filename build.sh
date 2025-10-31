#!/usr/bin/env bash
# build.sh

set -o errexit  # Detiene el script si ocurre un error

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
