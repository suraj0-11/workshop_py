class Vehicle:
    def vehicle_info(self):
        print("inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside car class")

car = Car()

car.vehicle_info()
car.car_info()
