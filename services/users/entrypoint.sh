#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

gunicorn --chdir ./project/api buscador_fichas:buscador_fichas -b 0.0.0.0:5000 -t 100 --reload
