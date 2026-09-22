#!/usr/bin/env bash


# Install dependencies 
pip install -r requirements.txt

# collect static files
python manage.py collectstatic --noinput

# apply database migrations
python manage.py migrate