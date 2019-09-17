#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z users-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"
gunicorn app.buscar_fichas:app --host 0.0.0.0
