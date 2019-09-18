#  base image
FROM postgres:11.2-alpine

WORKDIR /user/src/database
# run create.sql on init
ADD ./create.sql /docker-entrypoint-initdb.d

USER postgres

COPY ./fichas_dina.dump /user/src/database/fichas_dina.dump

#CMD ["psql fichas_dina < fichas_dina.dump"]
#CMD ["psql", "fichas_dina < /user/src/database/fichas_dina.dump"]
CMD ["pg_restore", "-U postgres -d fichas_dina /user/src/database/fichas_dina.dump"]
