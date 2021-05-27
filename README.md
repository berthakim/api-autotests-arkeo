# Autotests for API Meteo Stations

tested web-app url:
source-code of app: in this repository (folder "API_meteo")

Tools: Django 3.2.3, Django Rest Framework 3.12.4, PyTest

In order to connect to the OWM API:
1. in the project folder create the python file and name in config.py
2. in the config.py file write the variable <secret_key_settings> and assign to it your SECRET_KEY:
    secret_key_settings = "your-secret-key-for-django-settings"

To start an API application: in terminal (or cmd) place in "API_meteo" folder and run the django app:
> python manage.py runserver

To launch autotests type in the same directory:
> pytest test_api_basic.py  // to basic tests (connection, requests. data types)
> pytest test_api_performance.py  // performance tests
> python test_api_e2e.py  // end-to-end test-case

#### Structure of this project:

- folder "API_meteo" - contain API Django web application
- folder "API_meteo_autotests" - tests for API_meteo app
  - folder 
  - folder

This API app is based on Django REST Framework tutorial:
https://www.django-rest-framework.org/tutorial/quickstart/
