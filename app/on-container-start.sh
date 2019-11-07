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

echo "============================================================== cd into app"
echo ""
echo ""
echo ""
echo ""
echo ""
cd app
ls -alt
echo "============================================================== Create migrations based on django models"
echo ""
echo ""
echo ""
echo ""
echo ""
python manage.py makemigrations

echo "============================================================== Migrate created migrations to database"
echo ""
echo ""
echo ""
echo ""
echo ""
python manage.py migrate

#echo "============================================================== Collect Static "
#echo ""
#echo ""
#echo ""
#echo ""
#echo ""
#python manage.py collectstatic --no-input --clear


if [ "$DEBUG" == True ]; then
    echo "============================================================== create superuser "
    echo ""
    echo ""
    echo ""
    echo ""
    echo ""
    echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'pass')" | python manage.py shell

fi

echo "============================================================== Start the server"
echo ""
echo ""
echo ""
echo ""
echo ""
python manage.py runserver
#gunicorn --reload app.wsgi

exec "$@"
