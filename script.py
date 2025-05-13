import pandas as pd
from sodapy import Socrata

# example number plate: WVFS21
if __name__ == "__main__":

    # Connecting to opendata API
    client = Socrata("opendata.rdw.nl", None)

    # querying database using number plate provided by the user
    car_registration = input("enter registration number (without dashes): ")
    result = client.get("m9d7-ebf2", kenteken = car_registration)[0]

    #printing the row return
    for x in result:
        print(x, ":", result[x])