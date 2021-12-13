import pytest
import allure
from requests import HTTPError
from hamcrest import assert_that, equal_to, empty, is_in
from tests.clients.api_client import ApiClient
from tests.helpers.help_funcs import create_station


class TestApiMeteoDelete:

    def test_delete_station_success(self):
        new_station = create_station()
        new_station_id = {"station_id": new_station.get("id")}

        resp = ApiClient().delete_by_id(params=new_station_id)
        print("\nDeleted station:", new_station)

        assert_that(actual=resp.text,
                    matcher=empty(),
                    reason=f'Deleted station should return an empty value but was {resp.text}')

        assert_that(actual=resp.status_code,
                    matcher=is_in([200, 201, 204]),
                    reason=f'Response status should be in [200, 201, 204]'
                           f' but was {resp.status_code}')

    @allure.title("Delete a station with an invalid _id: DELETE request to /station/")
    def test_delete_station_with_an_invalid_id_should_fail(self):
        data = {"station_id": -100}

        response = ApiClient().delete_by_id(params=data)

        assert_that(actual=response.status_code,
                    matcher=equal_to(404),
                    reason=f"Failed to delete a station with code {response.status_code}")

    def test_station_should_not_exist_after_deletion(self):
        new_station = create_station()
        new_station_id = {"station_id": new_station.get("id")}

        resp = ApiClient().delete_by_id(params=new_station_id)
        print("\nDeleted station:", new_station, resp)

        try:
            ApiClient().get_by_id(params=new_station_id)
        except HTTPError:
            print("Station was deleted successfully")

    # def test_should_successfully_delete_nameless_station(self):
        # pass
