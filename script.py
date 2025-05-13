import pandas as pd
from sodapy import Socrata
import random
# example number plates: X360KN, 47SXGX, 60PJR3

NUM_PARKING_SPOTS = 8

class ParkingSpot:
    def __init__(self):
        self.car_parked_license = None
        self.taken = False

class APIService:
    def get_car_info(self, registration_number: str):

        # Connecting to opendata API
        client = Socrata("opendata.rdw.nl", None)
        result = client.get("m9d7-ebf2", kenteken=registration_number)[0]

        # Printing car info
        for x in result:
            print(x, ":", result[x])
        return result

class CameraSensor:
    def get_license_plate(self):

        # Getting license plate from the user
        license_plate = input("enter registration number (without dashes): ")
        return license_plate

if __name__ == "__main__":

    APIService = APIService()
    CameraSensor = CameraSensor()

    # Create a list of empty parking spaces
    parking_spots = []
    for i in range(NUM_PARKING_SPOTS):
        parking_spots.append(ParkingSpot())

    for x in range(3):
        arriving_car = CameraSensor.get_license_plate()
        APIService.get_car_info(arriving_car)

        while True:
            spot_chosen = random.randint(0, NUM_PARKING_SPOTS - 1)
            if parking_spots[spot_chosen].taken == True:
                continue
            else:
                break
        parking_spots[spot_chosen].taken = True
        parking_spots[spot_chosen].car_parked_license = arriving_car

    for i in range(len(parking_spots)):
        if parking_spots[i].taken == True:
            print("Parking Spot", i, "Taken by", parking_spots[i].car_parked_license)
        else:
            print("Parking Spot", i, "Free")