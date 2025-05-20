class CameraSensor:
    def __init__(self):
        self.car_list = open("example_cars.txt")
    def input_license_plate(self):

        # Getting license plate from the user
        license_plate = input("enter registration number (without dashes): ")
        return license_plate

    def get_next_license_plate(self):
        return (self.car_list.readline()).strip()
