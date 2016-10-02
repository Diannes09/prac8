"""
CP1404/CP5632 Practical
Car class
"""
import random

class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0.00):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        price_per_km = 1.2
        super().__init__(name, fuel)

        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        price_per_km = 1.2
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        price_per_km = 1.2
        return price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

class Oldcar(Car):
    """ represent an unreliable car object """
    def __init__(self, name, fuel, reliability=50):
        price_per_km = 1.2
        super().__init__(name, fuel)

        self.current_fare_distance = 0

        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.reliability = reliability
        self.drivability = random.randint(0, 100)


    def __str__(self):
        price_per_km = 1.2
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), price_per_km,
                                                             self.current_fare_distance)
    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def get_fare(self):
        """ get the price for the taxi trip """
        price_per_km = 1.2
        return price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if self.drivability < self.reliability:
            print ("Taxi can not be driven today")

        else:
            distance_driven = super().drive(distance)
            self.current_fare_distance += distance_driven
            return distance_driven

class SilverServiceTaxi(Car):

    def __init__(self, name="", fuel=0.00, fanciness=4.0):
        super().__init__(name, fuel, fanciness)
        """ initialise a Car instance """

        self.name = name
        self.fuel = fuel
        self.odometer = 0
        self.fanciness = fanciness
        self.flagfall = 4.5

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def get_fare(self):
        """ get the price for the taxi trip """
        price_per_km = 1.2
        silver_price_per_km = price_per_km * 4
        return price_per_km * self.current_fare_distance

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven