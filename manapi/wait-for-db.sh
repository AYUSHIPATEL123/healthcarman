#!/bin/sh
set -e

echo "⏳Waiting for MySQL at $DB_HOST:$DB_PORT..."

until nc -z "$DB_HOST" "$DB_PORT"; do 
    sleep 1
done 

echo "✅MySQL is up - executing command"

exec "$@"