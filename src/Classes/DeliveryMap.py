import operator


class DeliveryMap:
    # constructor

    def __init__(self):
        self.map_of_town = set()

    # methods

    def deliver_pizza(self, coordinate):
        self.map_of_town.add(coordinate)

    def get_final_size(self):
        return len(self.map_of_town)

