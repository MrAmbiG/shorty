gajuambi#!/bin/bash
cd shorty
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0 8000
# daphne shorty.asgi:application -b 0 -p 8000