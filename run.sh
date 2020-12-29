#!/bin/bash
cd shorty
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
# daphne shorty.asgi:application -b 0.0.0.0 -p 8001
daphne shorty.asgi:application -b 0 -p 8001