

class Coordinate(object):

    # constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # methods
    def move_up(self):
        self.y += 1

    def move_down(self):
        self.y -= 1

    def move_right(self):
        self.x += 1

    def move_left(self):
        self.x -= 1

    # return string value -- used for testing
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'

    # printing/formatting the output of a data structure
    def __repr__(self):
        return '({s.x!r}, {s.y!r})'.format(s=self)

    # will let you use coordinate objects in a hash
    def __hash__(self):
        return hash(repr(self))

    # allow coordinate objects to be compared to one another (for the hash)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

