class Vehicle:
    def __init__(self, mileage, max_speed=150):
        self.mileage = mileage
        self.max_speed = max_speed
        self.gadgets = []


# Create a class called Vehicle.
# Upon initialization, it should receive max_speed (integer, optional; 150 by default) and mileage (number).
# Create an instance variable called gadgets - an empty list by default.
#
#
# Test code:
car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)

#
# Expected output:
# 150
# 20
# []
# ['Hudly Wireless']
