from src.Classes.Coordinate import Coordinate


class Deliverer:
    # constructor

    def __init__(self, name):
        self.name = name
        self.current_coordinate = Coordinate()

    # getter

    def get_cc(self):
        return Coordinate(self.current_coordinate.x, self.current_coordinate.y)

    # methods

    def move_deliverer(self, direction):
        if direction == '^':
            self.current_coordinate.move_up()
        elif direction == 'v':
            self.current_coordinate.move_down()
        elif direction == '<':
            self.current_coordinate.move_left()
        elif direction == '>':
            self.current_coordinate.move_right()

    def __repr__(self):
        return "Name: % s | Current Coordinate: % s" % (self.name, self.current_coordinate)

    def __str__(self):
        return "% s" % self.name
