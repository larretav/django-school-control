#!/bin/sh

# echo 'Running collecstatic...'
# python manage.py collectstatic --no-input --settings=config.settings.production

# echo 'Applying migrations...'
# python manage.py wait_for_db --settings=config.settings.production
# python manage.py migrate --settings=config.settings.production

echo 'Running server...'
gunicorn --env DJANGO_SETTINGS_MODULE=django_school_control.settings django_school_control.wsgi:application --bind 0.0.0.0:$PORT