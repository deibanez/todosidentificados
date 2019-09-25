#s script is run when the docker container is built
# it imports the base database structure and create the database for the tests

DATABASE_NAME="fichas_dina"
DB_DUMP_LOCATION="/tmp/psql_data/structure.sql"

echo "*** CREATING DATABASE ***"

# create default database
psql <<EOSQL
  CREATE DATABASE "$DATABASE_NAME";
  GRANT ALL PRIVILEGES ON DATABASE "$DATABASE_NAME" TO postgres;
EOSQL

echo "chan chan"
# clean sql_dump - because I want to have a one-line command

# remove indentation
#sed "s/^[ \t]*//" -i "$DB_DUMP_LOCATION"

# remove comments
#sed '/^--/ d' -i "$DB_DUMP_LOCATION"

# remove new lines
#sed ':a;N;$!ba;s/\n/ /g' -i "$DB_DUMP_LOCATION"

# remove other spaces
#sed 's/  */ /g' -i "$DB_DUMP_LOCATION"

# remove firsts line spaces
#sed 's/^ *//' -i "$DB_DUMP_LOCATION"

# append new line at the end (suggested by @Nicola Ferraro)
#sed -e '$a\' -i "$DB_DUMP_LOCATION"

echo "chan chan "
# import sql_dump
psql "$DATABASE_NAME" < "$DB_DUMP_LOCATION";


echo "*** DATABASE CREATED! ***"
