#!/bin/bash
# Create a docker image
docker build -t web_scraping:v1.1 .
# Execute docker container
docker run web_scraping:v1.1