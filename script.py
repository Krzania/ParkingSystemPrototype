import pandas as pd
from sodapy import Socrata
import random
from parking_info import *
from api_service import *
from camera_sensor import *
# example number plates: X360KN, 47SXGX, 60PJR3
# trailer problem?

if __name__ == "__main__":

    APIService = APIService()
    CameraSensor = CameraSensor()
    ParkingInfo = ParkingInfo()

    for x in range(60):
        arriving_car = CameraSensor.input_license_plate()
        APIService.get_car_info(arriving_car)
        ParkingInfo.park_car(arriving_car)

    ParkingInfo.print_parking_info()