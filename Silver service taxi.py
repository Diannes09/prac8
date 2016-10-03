from taxi import SilverServiceTaxi
from taxi import Car
from taxi import Taxi

def main():
    silver_service = SilverServiceTaxi("Hummer", 200)
    silver_service.drive(20)
    silver_service.get_fare()
    silver_service.odometer
    silver_service.flagfall

    print("{}, fare ${:.2f}".format(silver_service, silver_service.get_fare()))

main()