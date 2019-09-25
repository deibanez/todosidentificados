FROM postgres:11.2-alpine

RUN mkdir -p /tmp/psql_data/

COPY structure.sql /tmp/psql_data/
COPY init_docker_postgres.sh /docker-entrypoint-initdb.d/

RUN chmod +x /tmp/psql_data/structure.sql
