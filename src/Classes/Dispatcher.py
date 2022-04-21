from src.Classes.Deliverer import Deliverer


class Dispatcher:
    # constructor
    def __init__(self, my_file, delivery_map, deliverers):
        self.my_file = my_file
        self.delivery_map = delivery_map
        self.deliverers = deliverers
        self.deliver_to_first_house()



    def complete_all_deliveries(self):
        total = len(self.deliverers)
        current = 0
        f = open(self.my_file)
        while 1:
            char = f.read(1)
            if not char:
                break
            self.move_and_deliver(char, current)
            if current < total-1:
                current += 1
            elif current >= total-1:
                current = 0
        f.close()

    def deliver_to_first_house(self):
        for deliverer in self.deliverers:
            self.delivery_map.deliver_pizza(deliverer.get_cc())

    def move_and_deliver(self, direction, index):
        current_deliverer = self.deliverers[index]
        current_deliverer.move_deliverer(direction)
        self.delivery_map.deliver_pizza(current_deliverer.get_cc())

    def number_unique_houses(self):
        return self.delivery_map.get_final_size()


