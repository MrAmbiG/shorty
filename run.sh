#!/bin/bash
cd shorty
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 127.0.0.1:8000