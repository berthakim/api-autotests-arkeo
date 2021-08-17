import pytest
import requests


# offline (if you launch the app in your local machine)
url_local = "http://127.0.0.1:8000/stations"
# online (if you use the heroku web site)
url_heroku = ""

url = url_local


def test_check_status_code_is_200():
    response = requests.get(url)
    assert response.status_code == 200, \
        f"Connection not succeded"
    # print("\nResponse status code:", response.status_code)


def test_check_content_type_is_json():
    response = requests.get(url)
    assert response.headers["Content-Type"] == "application/json", \
        "The response body is not in JSON format"
    # print("\nContent-Type:", response.headers["Content-Type"])


def test_check_name_of_first_stations_is_adalvik():
    response = requests.get(url)
    response_body = response.json()
    assert response_body[0]["name"] == "Adalvik", \
        "Value of variable 'name' in response's body is not 'London'"
    # print("\nFirst station name is", response_body[0]["name"])
