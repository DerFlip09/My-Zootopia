import json
import requests


API_KEY = "4EvovkZHfIDIkocKnLoO1Q==zLCf47tkEv0Ibdgb"
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


def get_file_data(filename: str) -> str:
    with open(filename, "r") as file:
        webpage = file.read()
        return webpage


def write_file(filename: str, text=None):
    with open(filename, "w") as handle:
        handle.write(text)
    print(f"Webpage successfully generated to file {filename}")


def get_skin_type_from_user(data):
    while True:
        skin_type = input("Choose a skin type or press Enter for nothing: ")
        if skin_type not in get_skin_types_from_data(data):
            print("Choose one of the available skin types")
        else:
            return skin_type


def get_skin_types_from_data(data):
    skin_types = []
    for animal in data:
        skin_types.append(animal["characteristics"].get("skin_type"))
    return "\n".join(set(skin_types)) + "\nAll"


def get_animal_info(animal: dict) -> dict:
    """
    Extracts relevant information about an animal.

    :param animal: Animal data as a dictionary.
    :returns: Filtered dictionary containing 'Name', 'Diet', 'Location', and 'Type'.
    """
    animal_info = {
        "Name": animal.get("name"),
        "Diet": animal["characteristics"].get("diet"),
        "Location": animal.get("locations")[0],
        "Type": animal["characteristics"].get("type"),
        "Weight": animal["characteristics"].get("weight"),
        "Lifespan": animal["characteristics"].get("lifespan"),
        "Skin Type": animal["characteristics"].get("skin_type")
    }
    animal_info = dict([(key, value) for key, value in animal_info.items() if value])
    return animal_info


def serialize_animal(animal: dict) -> str:
    """
    Serializes an animal's information into an HTML list item.

    :param animal: Animal data as a dictionary.
    :returns: HTML string representing the animal's information.
    """
    html_string = ""
    information = get_animal_info(animal)
    html_string += '<li class="cards__item">'
    html_string += f'<div class="card__title">{information["Name"]}</div>'
    html_string += '<p class="card__text">'
    html_string += '<ul class="animal__information">'
    for key, value in information.items():
        if key == "Name":
            pass
        else:
            html_string += f'<li class="item">{key}: {value}</li>\n'
    html_string += '</ul></p></li>'
    return html_string


def get_all_animal_data_as_string(data) -> str:
    """
    Converts a list of animal data into an HTML string.

    :param data: List of animal data dictionaries.
    :param skin_type: For filtering the Webpage
    :returns: HTML string containing all animals' information.
    """
    html_string = ''
    for animal in data:
        html_string += serialize_animal(animal)
    return html_string


def main():
    """
    Loads animal data, generates the updated HTML, and writes it to a file.
    """
    animal_data = get_data_from_api_by_name("fox")
    new_text = get_all_animal_data_as_string(animal_data)
    webpage = get_file_data("animals_template.html")
    updated_page = webpage.replace("__REPLACE_ANIMALS_INFO__", new_text)
    write_file("animals.html", updated_page)


if __name__ == "__main__":
    main()
