import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def get_animal_info(animal):
    animal_info = {
        "Name": animal.get("name"),
        "Diet": animal["characteristics"].get("diet"),
        "Location": animal.get("locations")[0],
        "Type": animal["characteristics"].get("type")
    }
    animal_info = dict([(key, value) for key, value in animal_info.items() if value])
    return animal_info


def get_all_animal_data_as_string(data):
    html_string = ''
    for animal in data:
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


def main():
    animal_data = load_data("animals_data.json")
    new_text = get_all_animal_data_as_string(animal_data)
    with open("animals_template.html", "r") as file:
        webpage = file.read()
        updated_page = webpage.replace("__REPLACE_ANIMALS_INFO__", new_text)
        with open("animals.html", "w") as file:
            file.write(updated_page)


if __name__ == "__main__":
    main()