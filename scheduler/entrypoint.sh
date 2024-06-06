#!/bin/bash

# Initialize the database
airflow db init

# Create an admin user if it doesn't exist
airflow users create \
    --username stingrae \
    --firstname worthy \
    --lastname rae \
    --role Admin \
    --email worthyrae@gmail.com \
    --password kraken

airflow webserver --port 8080 &
airflow scheduler &

# Keep the container running
tail -f /dev/null




