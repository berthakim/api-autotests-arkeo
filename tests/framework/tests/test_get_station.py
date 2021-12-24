import pytest
from hamcrest import assert_that, equal_to, not_none
from framework.clients.api_client import ApiClient
from framework.helpers.help_funcs import create_station


class TestApiMeteoGet:

    def test_get_station_success(self):
        new_station = create_station()  # arrange
        new_station_id = {"station_id": new_station.get("id")}

        station = ApiClient().get_by_id(params=new_station_id).json()
        print(station)

        assert_that(actual=station,
                    matcher=not_none(),
                    reason=f"Station's name shouldn't be empty (not none value) but was")

    def test_get_station_should_return_correct_name(self):
        new_station = create_station()  # arrange
        new_station_id = {"station_id": new_station.get("id")}

        station = ApiClient().get_by_id(params=new_station_id).json()
        print(station)

        assert_that(actual=station.get("name"),
                    matcher=equal_to(new_station.get("name")),
                    reason=f"Station's name should be equal to {new_station.get('name')}"
                           f"but was {station.get('name')}")

    def test_get_station_should_return_correct_region(self):
        new_station = create_station()  # arrange
        new_station_id = {"station_id": new_station.get("id")}

        station = ApiClient().get_by_id(params=new_station_id).json()
        print(station)

        assert_that(actual=station.get("region"),
                    matcher=equal_to(new_station.get("region")),
                    reason=f"Station's name should be equal to {new_station.get('region')}"
                           f"but was {station.get('region')}")

    def test_type_of_content_should_be_json(self):
        new_station = create_station()  # arrange
        new_station_id = {"station_id": new_station.get("id")}

        station = ApiClient().get_by_id(params=new_station_id)
        print(station)

        assert station.headers["Content-Type"] == "application/json", \
            "The response body is not of JSON format"
