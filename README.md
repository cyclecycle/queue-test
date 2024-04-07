# Run

docker compose up

## Scale workers

docker compose up --scale worker=2

# Test

docker compose exec test pytest

# Connect to DB

docker compose exec db psql -U postgres