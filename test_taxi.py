from taxi import Taxi
from taxi import Car

def main():
    new_cab = Taxi("Prius 1", 100)
    new_cab.drive(60)
    new_cab.get_fare()
    new_cab.odometer

    print("{}, fare ${}".format(new_cab, new_cab.get_fare()))

main()

