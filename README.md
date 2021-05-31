# Autotests for API Meteo Stations

tested web-app url:
source-code of app: in this repository (folder "API_meteo")

Tools: Django 3.2.3, Django Rest Framework 3.12.4, PyTest

In order to connect to the OWM API:
1. in the project folder create the python file and name in config.py
2. in the config.py file write the variable <secret_key_settings> and assign to it your SECRET_KEY:
    ```secret_key_settings = "your-secret-key-for-django-settings"```


How to launch the tests:

1. If you launch the app in your local machine:
2. If you use the web link

1. This API application was deployed on Heroku server, so You may view it by opening the following link:
> 
2. or You can launch this app locally in your machine. In order to start an app You may type the following:
    ```python manage.py runserver```
    (In terminal (or cmd), from "API_meteo" folder)


To launch autotests type in the same directory:
    ```pytest test_api_basic.py```  // to basic tests (connection, requests. data types)
    ```pytest test_api_performance.py```  // performance tests
    ```python test_api_e2e.py```  // end-to-end test-case

#### Structure of this project:

- folder "API_meteo" - contain API Django web application
- folder "API_meteo_autotests" - tests for API_meteo app
  - folder 
  - folder

This API app is based on Django REST Framework tutorial:
https://www.django-rest-framework.org/tutorial/quickstart/

Meteo Stations' data source:
https://en.vedur.is/weather/stations/?t=1

Bibliography for tests:
https://peter-jp-xie.medium.com/scale-up-rest-api-functional-tests-to-performance-tests-in-python-3239859c0e27

