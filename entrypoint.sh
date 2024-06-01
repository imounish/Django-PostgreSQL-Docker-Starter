#!/bin/bash
echo "Creating Migrations..."
python manage.py makemigrations usersapp
echo ====================================

echo "Starting Migrations..."
python manage.py migrate
echo ====================================

echo "Creating Super User..."
python manage.py makesuperuser
echo ====================================

echo "Starting Server..."
python manage.py runserver 0.0.0.0:8000