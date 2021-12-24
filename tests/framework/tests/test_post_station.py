import pytest
import allure
from requests import HTTPError
from hamcrest import assert_that, equal_to, not_none
from framework.clients.api_client import ApiClient


class TestApiMeteoGet:

    @allure.title("Test: post new station successfully")
    def test_post_station_success(self):
        data = {
            "name": "test station",
            "region": "test region",
            "st_type": "Manned synoptic station",
            "lat": 0.0, "lon": 0.0,
            "obs_beginning": 1900,
        }

        resp = ApiClient().post_station(data).json()
        print(resp)

        assert_that(actual=resp.get("name"),
                    matcher=not_none(),
                    reason='Name of station should not be empty (none) but was')

        assert_that(actual=resp.get("name"),
                    matcher=equal_to(data["name"]),
                    reason=f'Name of station should be equal to {data["name"]}'
                           f'but was {resp.get("name")}')

    def test_post_station_without_region_should_fail(self):
        data = {
            "name": "test name",
            "st_type": "Manned synoptic station",
            "lat": 0.0, "lon": 0.0,
            "obs_beginning": 1900,
        }

        with pytest.raises(HTTPError) as err:
            resp = ApiClient().post_station(data)
            assert resp == err

    def test_post_not_allowed_type_should_fail(self):
        data = {
            "name": "test name",
            "region": "test region",
            "st_type": "Test wrong type",
            "lat": 0.0, "lon": 0.0,
            "obs_beginning": 1900,
        }

        with pytest.raises(HTTPError) as err:
            resp = ApiClient().post_station(data)
            assert resp == err
