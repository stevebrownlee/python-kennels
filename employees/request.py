import animals


ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog"
    }
]


def get_all_animals(req):
    return ANIMALS

def get_single_animal(id):
    requested_animal = None

    for animal in ANIMALS:
        if animal["id"] == id:
            requested_animal = animal

    return requested_animal

def create_animal(req):
    return ANIMALS

def update_animal(req):
    return ANIMALS

def delete_animal(req):
    return ANIMALS
