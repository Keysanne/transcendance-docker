#!/bin/bash

python3 mysite/manage.py makemigrations && python3 mysite/manage.py migrate
exec "$@"
