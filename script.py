import pandas as pd
from sodapy import Socrata
import random
from parking_info import *
from api_service import *
from camera_sensor import *
# example number plates: X360KN, 47SXGX, 60PJR3
# trailer problem?

NUM_CARS_ARRIVING = 30
if __name__ == "__main__":

    APIService = APIService()
    CameraSensor = CameraSensor()
    ParkingInfo = ParkingInfo()

    for x in range(NUM_CARS_ARRIVING):
        arriving_car = CameraSensor.get_next_license_plate()
        print(arriving_car)
        APIService.get_car_info(arriving_car)
        ParkingInfo.park_car(arriving_car)

    ParkingInfo.print_parking_info()