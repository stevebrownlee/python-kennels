ANIMALS = [
    {
        "id": 1,
        "name": "Snickers",
        "species": "Dog",
        "location": 1,
        "customerId": 4,
        "status": "Assessment"
    },
    {
        "id": 2,
        "name": "Gypsy",
        "species": "Dog",
        "location": 1,
        "customerId": 2,
        "status": "Recreation"
    },
    {
        "id": 3,
        "name": "Blue",
        "species": "Cat",
        "location": 2,
        "customerId": 1,
        "status": "Treatment"
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


def update_animal(id, new_animal):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Update the value
            animal_index = index
            ANIMALS[index] = new_animal
            break

    if animal_index >= 0:
        return True

    return False


def delete_animal(id):
    # Initial -1 value for animal index, in case one isn't found
    animal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, animal in enumerate(ANIMALS):
        if animal["id"] == id:
            # Found the animal. Store the current index.
            animal_index = index

    # If the animal was found, use pop(int) to remove it from list
    if animal_index >= 0:
        ANIMALS.pop(animal_index)
