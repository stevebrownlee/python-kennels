DATABASE = {
    "animals": [
        {
            "id": 1,
            "name": "Snickers",
            "species": "Dog",
            "locationId": 1,
            "customerId": 4,
            "status": "Assessment"
        },
        {
            "id": 2,
            "name": "Gypsy",
            "species": "Dog",
            "locationId": 1,
            "customerId": 2,
            "status": "Recreation"
        },
        {
            "id": 3,
            "name": "Blue",
            "species": "Cat",
            "locationId": 2,
            "customerId": 1,
            "status": "Treatment"
        }
    ],
    "locations": [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ],
    "customers": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        },
        {
            "id": 2,
            "name": "Jenna Solis"
        },
        {
            "id": 3,
            "name": "Emily Lemmon"
        },
        {
            "id": 4,
            "name": "Bryan Nilson"
        }
    ],
    "employees": [
        {
            "id": 1,
            "name": "Ryan Tanay"
        },
        {
            "id": 2,
            "name": "Jenna Solis"
        },
        {
            "id": 3,
            "name": "Emily Lemmon"
        },
        {
            "id": 4,
            "name": "Bryan Nilson"
        }
    ]
}


def all(resource):
    return DATABASE[resource]


def retrieve(resource, id):
    found_resource = None

    resource_list = DATABASE[resource]
    for single_resource in resource_list:
        if single_resource["id"] == id:
            found_resource = single_resource

    return found_resource


def create(resource, new):
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    new["id"] = new_id
    DATABASE[resource].append(new)

    return new


def update(resource, id, new):
    found_index = -1

    resource_list = DATABASE[resource]
    for index, single_resource in enumerate(resource_list):
        if single_resource["id"] == id:
            found_index = index
            resource_list[index] = new
            break

    if found_index >= 0:
        return True

    return False


def delete(resource, id):
    resource_index = -1

    resource_list = DATABASE[resource]
    for index, item in enumerate(resource_list):
        if item["id"] == id:
            resource_index = index

    if resource_index >= 0:
        resource_list.pop(resource_index)
