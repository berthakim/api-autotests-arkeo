from framework.clients.api_client import ApiClient


def create_station():
    data = {
        "name": "test station",
        "region": "test region",
        "st_type": "Manned synoptic station",
        "lat": 0.0, "lon": 0.0,
        "obs_beginning": 1900,
    }
    station = ApiClient().post_station(data).json()
    return station
