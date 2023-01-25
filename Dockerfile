# Python base image to be able to run our project
FROM python:3.8.2

# Copy of all project code inside docker to be able to run it in Docker containers
COPY . .

# Establishment of the working directory
WORKDIR /.

# Installation of Python package requirements
RUN pip install -r requirements.txt

# Installation of Chromium browser
RUN apt-get update && apt-get install -y chromium

# Download of Chromium webdriver and binary files
RUN cd /opt && curl -SL https://github.com/adieuadieu/serverless-chrome/releases/download/v1.0.0-57/stable-headless-chromium-amazonlinux-2.zip > headless-chromium.zip && unzip headless-chromium.zip && curl -SL https://chromedriver.storage.googleapis.com/86.0.4240.22/chromedriver_linux64.zip > chromedriver.zip && unzip chromedriver.zip

# Exposure of a port to be able to send the results abroad
EXPOSE 3000

# Execution of the main project file
CMD [ "python", "src/main_docker.py"]