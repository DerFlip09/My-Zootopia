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


def print_animal_info(data):
    for animal in data:
        print(get_animal_info(animal) + "\n")


def main():
    animal_data = load_data("animals_data.json")
    print_animal_info(animal_data)


if __name__ == "__main__":
    main()