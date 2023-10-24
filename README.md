# performance_testing
performance_testing

How to use:
1) run databases using docker compose: `docker-compose -f setup/docker-compose/docker-compose-local.yml up`
2) create databases:
   1) MongoDB: run MongoDB and execute: `use performance_test_db`
   2) Postgresql: `createdb -h 127.0.0.1 -p5454 -Upostgres performance_test_db `
3) Create tables in database: `./manage.py migrate --database=postgres`
4) Generate some data to insert into the databases, so we have the same data for all databases. `./manage.py generate_data -m 1000 > ./generated_data.json`
5) Insert the generated data into all databases: `./manage.py insert_data ./generated_data.json`
6) Run performance tests: `./manage.py query_data`