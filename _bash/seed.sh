#!/bin/bash

cd ..

# curl -X POST -d "name=John Doe&email=johndoe@example.com&birthday=1990-01-01" http://localhost:8000/api/customer/register/

# The base URL for your Django API
API_URL="http://localhost:8000/api/customer/register"

# Define your customers here
declare -a customers=(
    "name=John Doe&email=johndoe@example.com&birthday=1990-05-02&wish_year=0"
    "name=Jane Smith&email=janesmith@example.com&birthday=1985-05-02&wish_year=0"
    "name=Alice Johnson&email=alicejohnson@example.com&birthday=1993-05-02&wish_year=0"
    "name=Michael Brown&email=michaelbrown@example.com&birthday=1988-05-01&wish_year=0"
    "name=Emily Davis&email=emilydavis@example.com&birthday=1992-05-12&wish_year=0"
)

# Loop through the customers and send a POST request for each one
for customer in "${customers[@]}"
do
   echo "Submitting customer: ${customer}"
   curl -X POST "${API_URL}" -d "${customer}"
   echo "" # New line for cleaner output
done

# End of script
