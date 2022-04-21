from src.Classes.Coordinate import Coordinate
from src.Classes.Deliverer import Deliverer
from src.Classes.DeliveryMap import DeliveryMap
from src.Classes.Dispatcher import Dispatcher


def main():
    run()


def run():
    fr1 = Dispatcher('Files/input.txt', DeliveryMap(), [Deliverer('Maria')])
    fr1.complete_all_deliveries()
    print('Maria delivered pizzas to {} houses'.format(fr1.number_unique_houses()))

    fr2 = Dispatcher('Files/input.txt', DeliveryMap(), [Deliverer('Maria'), Deliverer('Clovis'), Deliverer('Lily')])
    fr2.complete_all_deliveries()
    print('Maria and Clovis delivered pizzas to {} houses'.format(fr2.number_unique_houses()))


if __name__ == '__main__':
    main()
