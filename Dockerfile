# Python base image to be able to run our project
FROM python:3.8.2

# Copy of all project code inside docker to be able to run it in Docker containers
COPY . .

# Establishment of the working directory
WORKDIR /.

# Installation of project requirements
RUN pip install -r requirements.txt

# Exposure of a port to be able to send the results abroad
EXPOSE 3000

# Execution of the main project file
CMD [ "python", "src/main.py"]