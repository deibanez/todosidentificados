#  base image
FROM postgres:11.2-alpine

# run create.sql on init
ADD dump.sql /docker-entrypoint-initdb.d

