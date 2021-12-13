FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
# RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

# create root directory for our project in the container
RUN mkdir /meteo_api

# Set the working directory to /meteo_api
WORKDIR /meteo_api

# Copy the current directory contents into the container at /meteo_api
ADD . /meteo_api/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

COPY . .
