class Animal():

    def __init__(self, name, breed, status, location_id, customer_id, unique_id):
        self.id = unique_id
        self.name = name
        self.breed = breed
        self.status = status
        self.locationId = location_id
        self.customerId = customer_id
        self.location = None
        self.customer = None
