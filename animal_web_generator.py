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
    formatted_info = "\n".join(f"{key}: {value}" for key, value in animal_info.items() if value)
    return formatted_info


def get_all_animal_data_as_string(data):
    html_string = ""
    for animal in data:
        html_string += (f"{get_animal_info(animal)}\n\n")
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