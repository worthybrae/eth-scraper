#!/bin/bash

# Initialize the Airflow database
airflow db init

# Start the Airflow webserver
exec airflow webserver

