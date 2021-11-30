import pytest
import requests


class TestApiMeteoUserAuthorization:

    data = {"name": "StationZ",
            "lat": 100, "lon": 100,
            "start": 1882,
            "st_type": "Virtual station",
            "owner": "berthakim"}

    # negative test. Cannot post if not logged in: 403: Forbidden
    def test_user_cannot_add_object_via_post_if_logged_out(self):
        url = "http://127.0.0.1:8000/stations/"
        response = requests.post(url, json=self.data)
        assert response.status_code == 403,\
            "User can post an object when logged out but shouldnt"


    def test_user_cant_put_data_if_not_authorized(self):
        url_put = "http://127.0.0.1:8000/stations/1/"
        response = requests.put(url_put, self.data)
        assert response.status_code == 403, \
            f"User can put the data when logged out but shouldnt. SC: {response.status_code}"


    # Forbidden
    def test_user_cannot_delete_an_object_if_logged_out(self):
        url = "http://127.0.0.1:8000/stations/19"
        resp = requests.delete(url)
        assert resp.status_code == 403,\
        "Failed to delete an object with status code {resp.status_code}. You should probably log in"
