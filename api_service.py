from sodapy import Socrata

class APIService:
    def get_car_info(self, registration_number: str):

        # Connecting to opendata API
        client = Socrata("opendata.rdw.nl", None)
        result = client.get("m9d7-ebf2", kenteken=registration_number)[0]

        # Printing car info
        for x in result:
            print(x, ":", result[x])
        return result
