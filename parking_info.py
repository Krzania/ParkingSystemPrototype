from random import *
from parking_spot import *

#Total number of parking spots
NUM_PARKING_SPOTS = 8
random = Random()

class ParkingInfo:
    def __init__(self):

        # Create a list of empty parking spaces
        self.parking_spots = []
        for a in range(NUM_PARKING_SPOTS):
            self.parking_spots.append(ParkingSpot())

    # Park a car in a random parking spot
    def park_car(self, arriving_license_plate: str):
        while True:
            spot_chosen = random.randint(0, NUM_PARKING_SPOTS - 1)
            if self.parking_spots[spot_chosen].taken == True:
                continue
            else:
                break
        self.parking_spots[spot_chosen].taken = True
        self.parking_spots[spot_chosen].car_parked_license = arriving_license_plate

    def print_parking_info(self):
        for spot in self.parking_spots:
            if spot.taken == True:
                print("Parking Spot", self.parking_spots.index(spot), "taken by", spot.car_parked_license)