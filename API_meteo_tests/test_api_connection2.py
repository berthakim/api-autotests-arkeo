import pytest
import requests
from requests.auth import HTTPBasicAuth
import config_test as c


# # offline (if you launch the app in your local machine)
# url_local = "http://127.0.0.1:8000/stations"
# # online (if you use the heroku web site)
# url_heroku = ""

# url = url_local


class TestApiMeteoBasic:

    url = "http://127.0.0.1:8000/stations"
    response = requests.get(url)

    def test_check_status_code_is_200(self):
        assert self.response.status_code == 200, \
            f"Connection not succeded"
        # print("\nResponse status code:", response.status_code)


    def test_check_content_type_is_json(self):
        assert self.response.headers["Content-Type"] == "application/json", \
            "The response body is not in JSON format"
        # print("\nContent-Type:", response.headers["Content-Type"])


    def test_check_name_of_first_stations_is_adalvik(self):
        response_body = self.response.json()
        assert response_body[0]["name"] == "Adalvik", \
            "Value of variable 'name' in response's body is not 'London'"
        # print("\nFirst station name is", response_body[0]["name"])


class TestApiMeteoUserRequests:

    my_data = {
        "name": "Test Station",
        "lat": 65.6856,
        "lon": 18.1002,
        "start": 1881,
        "st_type": "Manned synoptic station",
        "owner": "berthakim"
    }

    # negative test. Cannot post if not logged in: 403: Forbidden
    def test_user_cannot_add_object_via_post_if_logged_out(self):
        url = "http://127.0.0.1:8000/stations/"
        response = requests.post(url, json=self.my_data)
        assert response.status_code == 403,\
            "User can post an object when logged out but couldn't"

    
    # positive test: Can post if logged in: 201: Success
    def test_user_can_add_object_via_post(self):  # 201: created
        url = "http://127.0.0.1:8000/stations/"
        response = requests.post(url, json=self.my_data,
                                 auth = HTTPBasicAuth('berthakim', '557878ars'))
        assert response.status_code == 201,\
            f"Failed post an object with status code {response.status_code}"


    def test_user_can_put_data(self):
        pass


    def test_user_can_delete_object(self):
        pass


class TestApiMeteoClientErrorResponses:

    # def test_should_return_403_because_user_is_logged_out(self):
    #     url = "http://127.0.0.1:8000/stations/"
    #     response = requests.post(url, json=self.my_data)
    #     assert response.status_code == 201  # Forbidden
    
    # 404 (Not Found): requested object (so page) doesn't existe 
    def test_should_return_404_because_unknown_path_was_requested(self):
        url = "http://127.0.0.1:8000/stations/200"
        response = requests.get(url)
        assert response.status_code == 404, \
            "Request of unknown path doesn't return a response with\
             a status code of HTTP 404 (not found)"


    # 405 (not allowed method): PATCH
    def test_should_return_405_because_patch_is_not_allowed(self):
        url = "http://127.0.0.1:8000/stations/"
        response = requests.patch(url, auth = HTTPBasicAuth('berthakim', 'c.api_app_password'))
        assert response.status_code == 405, \
            "Request with a non-allowed method doesn't return a response\
             with a status code of HTTP 405 (method not allowed), but should"


    # 405 (not allowed method): CONNECT
    def test_should_return_405_because_patch_is_not_allowed(self):
        url = "http://127.0.0.1:8000/stations/"
        response = requests.patch(url, auth = HTTPBasicAuth('berthakim', 'c.api_app_password'))
        assert response.status_code == 405, \
            "Request with a non-allowed method doesn't return a response\
             with a status code of HTTP 405 (method not allowed), but should"

    
    # 405 (not allowed method): OPTIONS
    # def test_should_return_405_because_patch_is_not_allowed(self):
    #     url = "http://127.0.0.1:8000/stations/"
    #     response = requests.patch(url, auth = HTTPBasicAuth('berthakim', '557878ars'))
    #     assert response.status_code == 405, \
    #         "Request with a non-allowed method doesn't return a response\
    #          with a status code of HTTP 405 (method not allowed), but should"

    
    # 405 (not allowed method): TRACE
    def test_should_return_405_because_patch_is_not_allowed(self):
        url = "http://127.0.0.1:8000/stations/"
        response = requests.patch(url, auth = HTTPBasicAuth('berthakim', '557878ars'))
        assert response.status_code == 405, \
            "Request with a non-allowed method doesn't return a response\
             with a status code of HTTP 405 (method not allowed), but should"


class TestCrash:
    """like very long texts to post/put or something"""
    pass

class TestLoad:
    """Load testing"""
    pass


class TestSecurity:
    """ Security tests"""
    pass


def test_post_some_data():
    pass

# DELETE
# 403 (Forbidden). Unuthorized user
url = "http://127.0.0.1:8000/stations/19"
def test_user_cannot_delete_an_object_if_logged_out():
    resp = requests.delete(url)
    assert resp.status_code == 403,\
    "Failed to delete an object with status code {resp.status_code}. You should probably log in"

# 204 (No Content) Resource deleted successfully
def test_user_can_delete_an_object_if_logged_in():
    response = requests.delete(url, auth = HTTPBasicAuth('berthakim', 'c.api_app_password'))
    assert response.status_code == 204,\
        f"Failed to delete an object with status code {response.status_code}"
        
# 404 (Not Found)
def test_should_be_404_if_user_delete_missing_object():
    resp = requests.delete(url, auth=HTTP('berthakim', 'c.api_app_password'))
