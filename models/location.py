class Location():

    def __init__(self, name, address = "", animals = 0):
        self.name = name

        if animals > 0:
            self.animals = animals

        if address != "":
            self.address = address