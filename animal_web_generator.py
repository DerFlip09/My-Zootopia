import json


def load_json_data(file_path: str):
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_file_data(filename: str) -> str:
    with open(filename, "r") as file:
        webpage = file.read()
        return webpage


def write_file(filename: str, text=None):
    with open(filename, "w") as handle:
        handle.write(text)
    print("File successfully written")


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
        "Type": animal["characteristics"].get("type")
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
    for key, value in information.items():
        if key == "Name":
            pass
        html_string += f'<strong>{key}:</strong> {value}<br/>\n'
    html_string += '</p></li>'
    return html_string


def get_all_animal_data_as_string(data) -> str:
    """
    Converts a list of animal data into an HTML string.

    :param data: List of animal data dictionaries.
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
    animal_data = load_json_data("animals_data.json")
    new_text = get_all_animal_data_as_string(animal_data)
    webpage = get_file_data("animals_template.html")
    updated_page = webpage.replace("__REPLACE_ANIMALS_INFO__", new_text)
    write_file("animals.html", updated_page)


if __name__ == "__main__":
    main()
