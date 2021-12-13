# API Meteo Stations + Autotests (pytest)

Start API service

1. Locally:
   - create and activate new virtual environment
   - ```pip install requirements.txt```
   - ```python manage.py migrate```
   - ```python manage.py createsuperuser```
   - ```python manage.py runserver```
3. Using Docker
   - ```docker-compose build```
   - ```docker-compose up -d```
   - then create a superuser: ```docker-compose exec web python manage.py createsuperuser```

Meteo Stations' data source:
https://en.vedur.is/weather/stations/?t=1
