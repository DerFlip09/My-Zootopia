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
    print(animal_info)
    return animal_info

data = load_data("animals_data.json")

for animal in data:
    get_animal_info(animal)