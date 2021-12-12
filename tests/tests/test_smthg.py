import pytest
import requests
from requests.auth import HTTPBasicAuth
import config_test as ct  # password

# offline (if you launch the app in your local machine)
url_local = "http://127.0.0.1:8000/stations/"

# online (if you use the heroku web site)
url_heroku = "http://meteo-stations-api/stations/"

url = url_local


# @pytest.mark.skip(reason="temporary delated")
class TestApiMeteoGet:
    url = "http://127.0.0.1:8000/stations"
    response = requests.get(url)

    # View one station: GET request to /stations/
    def test_should_successfully_response_to_a_get_request(self):
        assert self.response.status_code == 200, \
            f"Connection not succeded with code {response.status_code}"

    def test_returned_type_of_content_should_be_json(self):
        assert self.response.headers["Content-Type"] == "application/json", \
            "The response body is not in JSON format"

    def test_name_of_second_stations_should_be_akureyri(self):
        response_body = self.response.json()
        assert response_body[-2]["name"] == "Akureyri", \
            "Value of variable 'name' in response's body is not 'London'"


# @pytest.mark.skip(reason="temporary delated")
class TestApiMeteoFilterDataInGetRequests:
    url = "http://127.0.0.1:8000/stations"
    response = requests.get(url)

    # View station with one filter: GET request to /stations/
    # We know what there's 3 stations founded in 1882
    def test_should_show_3_stations_founded_in_1882(self):
        response_body = self.response.json()
        filtered = [i for i in response_body if i["start"] == 1882]
        assert len(filtered) == 3, "Must be 3 stations founded in 1882"

    # View stations with multiple filters: GET request to /stations/
    # We know what there's 1 station founded in 1882 and
    # having the type "Automated observational station" (AOS)
    def test_should_show_the_station_founded_in_1882_and_of_AOS_type(self):
        response_body = self.response.json()
        filtered = [i for i in response_body if i["start"] == 1882]
        filtered2 = [i for i in filtered if i["st_type"] == "Automated observational station"]
        assert len(filtered2) == 1, "Must be 1 station established in 1882 and with AOS type"


# @pytest.mark.skip(reason="temporary delated")
class TestApiMeteoPost:
    url = "http://127.0.0.1:8000/stations/"

    # Create an station with every field: POST request to /stations/
    def test_should_create_a_station_with_every_field(self):
        data = {"name": "NINA",
                "lat": 50, "lon": 50,
                "start": 1900,
                "st_type": "Manned synoptic station",
                "owner": "postgres"
                }

        response = requests.post(self.url, data=data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 201, \
            f"Failed post an object with status code {response.status_code}"

    # negative test
    # Create station with missing required fields: POST request to /stations/
    def test_shouldnt_create_a_station_if_request_have_missing_required_field(self):
        data = {"name": "StationX",
                "lat": 50, "lon": 50,
                "st_type": "Manned synoptic station",
                "owner": "berthakim"
                }

        response = requests.post(self.url, data=data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 400, \
            f"POST didn't response with client error code 400 but should\
            Response was {response.text} with code {response.status_code}"

    # create a station with wrong data type of one of the field
    def test_should_not_create_a_station_if_used_wrong_datatype(self):
        data = {"name": "StationX",
                "lat": 50, "lon": 50,
                "start": "nineteen ninety",
                "st_type": "Manned synoptic station",
                "owner": "berthakim"
                }

        response = requests.post(self.url, data=data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 400, \
            f"Acept wrong data type (str) for field 'start' but shouldnt"


# @pytest.mark.skip(reason="temporary delated")
class TestApiMeteoPut:

    # Update one field on a station: PUT request to /stations/ -- code
    def test_should_return_one_modified_field(self):
        url_put = "http://127.0.0.1:8000/stations/43/"
        data = {"name": "StationZ",
                "lat": 100, "lon": 100,
                "start": 1882,
                "st_type": "Virtual station",
                "owner": "berthakim"}
        response = requests.put(url_put, data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        response_body = response.json()
        assert response_body["st_type"] == "Virtual station", \
            f"Station type wasn't changed, but should. Status code: {response.status_code}"

    # Update multiple fields on a station: PUT request to /stations/
    def test_should_return_three_edited_fields(self):
        url_put = "http://127.0.0.1:8000/stations/37/"
        data = {"id": 37,
                "name": "StationZ",
                "lat": 58.3850934289, "lon": 4.2358093,
                "start": 2010,
                "st_type": "Virtual station",
                "owner": "berthakim"}
        response = requests.put(url_put, data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        response_body = response.json()
        assert response_body == data, f"Field(s) wasn't changed, but should. {response.status_code}"

    # Update a station with missing name: PUT request to /stations/
    # fixture: create an unnamed station
    def test_should_give_a_name_to_unnamed_station(self):
        url_put = "http://127.0.0.1:8000/stations/44/"
        data = {"name": "Bon Jovi",
                "lat": 58.3850934289, "lon": 4.2358093,
                "start": 1964,
                "st_type": "Virtual station",
                "owner": "berthakim"}
        response = requests.put(url_put, data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        response_body = response.json()
        assert response_body["name"], f"Station still haven't name. {response.status_code}"

    # Update a station with no fields to update: PUT request to /station/
    def test_put_request_with_no_changes_shouldnt_do_any_modificaton(self):
        url_put = "http://127.0.0.1:8000/stations/44/"
        data = {"id": 44,
                "name": "Bon Jovi",
                "lat": 58.3850934289, "lon": 4.2358093,
                "start": 1964,
                "st_type": "Virtual station",
                "owner": "berthakim"}
        response = requests.put(url_put, data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        response_body = response.json()
        assert response_body == data, f"Field(s) was changed but shouldnt. {response.status_code}"

    # Update a station with an invalid _id: PUT request to /station/
    def test_should_return_404_due_to_an_invalid_id(self):
        url_put = "http://127.0.0.1:8000/stations/1001/"
        data = {"id": 44,
                "name": "Bon Jovi 2",
                "lat": 58.3850934289, "lon": 4.2358093,
                "start": 1964,
                "st_type": "Virtual station",
                "owner": "berthakim"}
        response = requests.put(url_put, data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 404, f"Put request should return code 404 " \
                                            f"but {response.status_code} was given"


# @pytest.mark.skip(reason="temporary delated")
class TestApiMeteoDelete:
    url_post = f"http://127.0.0.1:8000/stations/"

    # Delete a station: DELETE request to /station/
    # fixture: should existe a statiosn with id 48 (or whatever in the url)
    # or delete the last one (f'http://127.0.0.1:8000/stations/{"index-of-last-station"}')  # see index in GET
    def test_station_shouldnt_exist_after_it_was_deleted(self):
        # create station
        data = {"name": "",
                "lat": 50, "lon": 50,
                "start": 1900,
                "st_type": "Manned synoptic station",
                "owner": "berthakim"
                }
        response = requests.post(self.url_post, data=data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        r_body = response.json()

        url = f"{self.url_post}{r_body['id']}"
        response = requests.delete(url, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 204, f"Failed to delete a station with code {response.status_code}"

    # закрепим проверку удаления станции (перепроверим предыдущий тест)
    def test_revise_deleting_test(self):
        url = f"{self.url_post}80"
        response = requests.get(url)
        assert response.status_code == 404, "Page found or responsed with not 404 code, but shouldnt"

    # Delete a station with an invalid _id: DELETE request to /station/
    def test_delete_station_with_an_invalid_id_shouldnt_find_page(self):
        url_del = f"{self.url_post}1001"
        response = requests.delete(url_del, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 404, f"Failed to delete a station with code {response.status_code}"

    # Delete a station with missing name: DELETE request to /station/
    # fixture: should existe a station  # with id 80 (or whatever) in the url
    def test_should_succefully_delete_indicated_unnamed_station(self):
        # create station
        data = {"name": "",
                "lat": 50, "lon": 50,
                "start": 1900,
                "st_type": "Manned synoptic station",
                "owner": "berthakim"
                }
        response = requests.post(self.url_post, data=data, auth=HTTPBasicAuth('berthakim', ct.api_password))
        r_body = response.json()

        # delete this station with missing name value
        url_del = f"{self.url_post}{r_body['id']}"
        response = requests.delete(url_del, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 204, \
            f"Failed to delete a station with missing 'name'. Code: {response.status_code}"


# TODO: je dois supprimer les enrigestrements faites pour tester
# la fonctionnalité de post request.


class TestApiMeteoNotAllowedRequests:
    url = "http://127.0.0.1:8000/stations/"

    def test_should_return_405_because_patch_is_not_allowed(self):
        response = requests.patch(self.url, auth=HTTPBasicAuth('berthakim', ct.api_password))
        assert response.status_code == 405, \
            "Request with a non-allowed method doesn't return a response\
             with a status code 405 (method not allowed), but should"
