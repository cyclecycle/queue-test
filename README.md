# API with Redis Queue

An example of a containerized setup for an API that uses a Redis Queue to process tasks asynchronously and a PostgreSQL database to store the results.

## Run

docker compose up

### Scale workers

docker compose up --scale worker=2

## Test

docker compose exec test pytest

## Connect to DB

docker compose exec db psql -U postgres