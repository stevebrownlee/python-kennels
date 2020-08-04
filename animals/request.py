ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat"
    }
]


def get_all_animals():
    return ANIMALS

def get_single_animal(id):
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(animal):
    max_id = ANIMALS[-1]["id"]
    new_id = max_id + 1
    animal["id"] = new_id
    ANIMALS.append(animal)

    return animal

def update_animal():
    return ANIMALS

def delete_animal():
    return ANIMALS
