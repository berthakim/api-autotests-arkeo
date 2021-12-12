FROM python:3.8

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /meteo_api

# Set the working directory to /meteo_api
WORKDIR /meteo_api

# Copy the current directory contents into the container at /meteo_api
ADD . /music_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
