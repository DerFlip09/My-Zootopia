from data_fetcher import get_data_from_api_by_name


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


def get_animal_name_from_user():
    name = input("Enter animal name: ").strip()
    return name


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


def generate_webpage_from_template(text, template_file):
    webpage = get_file_data(template_file)
    updated_page = webpage.replace("__REPLACE_ANIMALS_INFO__", text)
    write_file("animals.html", updated_page)


def main():
    """
    Loads animal data, generates the updated HTML, and writes it to a file.
    """
    name = get_animal_name_from_user()
    animal_data = get_data_from_api_by_name(name)
    if not animal_data:
        error_text = f'<h2>The animal <i>{name}</i> does not exist.</h2>'
        generate_webpage_from_template(error_text, "animals_template.html")
    else:
        new_text = get_all_animal_data_as_string(animal_data)
        generate_webpage_from_template(new_text, "animals_template.html")


if __name__ == "__main__":
    main()
