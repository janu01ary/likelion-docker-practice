#!/bin/bash

python manage.py migrate

python manage.py collectstatic

gunicorn imgproject.wsgi -b 0.0.0.0:8000