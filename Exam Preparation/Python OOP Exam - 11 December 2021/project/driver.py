from project.car.car import Car


class Driver:
    def __init__(self, name: str):
        self.name = name
        self.car = None     # object of type Car
        self.number_of_wins = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value.strip()) == 0:
            raise ValueError("Name should contain at least one character!")
        self.__name = value

    def set_car(self, car):
        if self.car is None:
            self.car = car
            result = f"Driver {self.name} chose the car {car.model}."
        else:
            self.car.is_taken = False
            old_car_model = self.car.model
            self.car = car
            result = f"Driver {self.name} changed his car from {old_car_model} to {car.model}."

        self.car.is_taken = True

        return result
