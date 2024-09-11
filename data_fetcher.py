import json
import requests



API_URL = "https://api.api-ninjas.com/v1/animals"


def load_json_data(file_path: str):
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_data_from_api_by_name(name):
    api_query = API_URL + '?name={}'.format(name)
    response = requests.get(api_query, headers={'X-Api-Key': API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)