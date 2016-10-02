from taxi import Taxi
from taxi import Car
from taxi import Oldcar

def main():
    unreliable_car = Oldcar("Taxi",50)
    unreliable_car.drive(40)
    unreliable_car.odometer
    unreliable_car.get_fare()

    print("{}, fare ${}".format(unreliable_car, unreliable_car.get_fare()))

main()