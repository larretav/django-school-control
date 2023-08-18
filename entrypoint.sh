#!/bin/sh

echo 'Running collecstatic...'
python manage.py collectstatic --no-input --settings=django_school_control.settings

# echo 'Applying migrations...'
# python manage.py wait_for_db --settings=django_school_control.settings
# python manage.py migrate --settings=django_school_control.settings

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=django_school_control.settings django_school_control.wsgi:application --bind 0.0.0.0:$PORT