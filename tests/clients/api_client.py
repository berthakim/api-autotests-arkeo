import requests
from requests.auth import HTTPBasicAuth
from tests.settings import URL, HEADERS, USER, PASSWORD


class ApiClient:

    def get_by_id(self, params, path="/stations/{station_id}"):
        path = path.format(**params)
        response = requests.get(
            url=f'{URL}{path}',
            headers=HEADERS,
        )
        response.raise_for_status()
        return response

    def post_station(self, data, path="/stations/"):
        auth = HTTPBasicAuth(USER, PASSWORD)
        response = requests.post(
            url=f'{URL}{path}',
            data=data,
            auth=auth
        )
        response.raise_for_status()
        return response

    def put_station(self, data, path="/stations/{station_id}"):
        auth = HTTPBasicAuth(USER, PASSWORD)
        response = requests.post(
            url=f'{URL}{path}',
            data=data,
            auth=auth
        )
        response.raise_for_status()
        return response

    def delete_by_id(self, params, path="/stations/{station_id}"):
        path = path.format(**params)
        auth = HTTPBasicAuth(USER, PASSWORD)
        response = requests.delete(
            url=f'{URL}{path}',
            auth=auth
        )
        # response.raise_for_status()
        return response

