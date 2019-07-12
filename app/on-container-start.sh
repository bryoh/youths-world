#!/bin/sh

#if [ "$DATABASE" = "postgres" ]
#then
    #echo "Waiting for postgres..."

    #while ! nc -z $SQL_HOST $SQL_PORT; do
      #sleep 0.1
    #done

    #echo "PostgreSQL started"
#fi
# Create migrations based on django models

echo "==============================================================="
ls
echo "==============================================================="
cd app
python manage.py makemigrations

echo "==================Migrate created migrations to database============================================="
# Migrate created migrations to database
python manage.py migrate

# Start gunicorn server at port 8000 and keep an eye for app code changes
# If changes occur, kill worker and start a new one

#python manage.py flush --no-input
#python manage.py migrate
echo "==================Collect Static ============================================="
#python manage.py collectstatic --no-input 

#python manage.py runserver
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

echo "==============================================================="
gunicorn app.wsgi 
#useradd wagtail
#chown -R wagtail /code

exec "$@"
