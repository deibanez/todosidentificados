#!/bin/bash

set -e

echo "Waiting for postgres..."

while ! nc -z localhost 5435; do
	  sleep 0.1
  done

  echo "PostgreSQL started"

  psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" -d fichas_dina -f fichas_dina.dump
