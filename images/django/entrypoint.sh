#!/bin/bash

python3 /code/images/django/mysite/back/manage.py makemigrations && python3 /code/images/django/mysite/back/manage.py migrate
exec "$@"
