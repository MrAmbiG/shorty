#!/bin/bash
python shorty/manage.py collectstatic --noinput
python shorty/manage.py makemigrations
python shorty/manage.py migrate
python shorty/manage.py runserver