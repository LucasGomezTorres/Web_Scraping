#!/bin/bash
# Create a docker image
docker build -t web_scraping:v1 .
# Execute docker container
docker run web_scraping:v1 /bin/bash 