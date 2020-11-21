#!/bin/bash
python shorty/manage.py collectstatic --noinput
python shorty/manage.py runserver 10.216.151.62:8000