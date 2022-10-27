#!/bin/bash
docker build -t web_scraping:v1 .
docker run web_scraping:v1