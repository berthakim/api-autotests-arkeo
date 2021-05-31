import requests
from requests.auth import HTTPBasicAuth

url = "http://127.0.0.1:8000/stations/"

my_data = {
    "name": "Adalvik",
    "lat": 66.369,
    "lon": 23.019,
    "start": 2014,
    "st_type": "Virtual station",
    "owner": "berthakim"
}

# response = requests.get(url,
#             auth = HTTPBasicAuth('berthakim', '557878ars'))
# print(response.status_code)

# response = requests.trace(url)
# print(response, end="\n\n")

# url = "http://127.0.0.1:8000/stations/200"
# response = requests.get(url)
# print(response.status_code)

# url = "http://127.0.0.1:8000/stations/"
# response = requests.patch(url, auth = HTTPBasicAuth('berthakim', '557878ars'))
# print(response)  # 405 Method Not Allowed

# response = requests.post(url, json=my_data)
# print(response)  # 403 Forbidden

# response = requests.get(url)
# print("headers:", response.headers, end="\n\n")
# print("text:", response.text, end="\n\n")
# print("json:", response.json, end="\n\n")


# url = "http://127.0.0.1:8000/stations/21"
# response = requests.delete(url)
# print(response.status_code)
# will return status code 403 - Forbidden
url = "http://127.0.0.1:8000/stations/19"
response = requests.delete(url, auth = HTTPBasicAuth('berthakim', '557878ars'))
print(response.status_code)
# will return 204 - No Content
# If you going to repete this request after recieving a successful response
# it will return 404 - Page Not Found 
