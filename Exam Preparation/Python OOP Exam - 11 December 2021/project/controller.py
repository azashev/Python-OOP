from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []      # contains all cars as objects
        self.drivers = []       # contains all drivers as objects
        self.races = []     # contains all races as objects

    def __check_if_car_exists_and_return_it(self, car_model: str):
        for car in self.cars:
            if car.model == car_model:
                return car

    def __find_and_return_last_car_of_given_type_if_not_taken(self, car_type: str):
        for car in self.cars[::-1]:
            if car.__class__.__name__ == car_type:
                if not car.is_taken:
                    return car

    def __check_if_driver_exists_and_return_it(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                return driver

    def __check_if_race_exists_and_return_it(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                return race

    @staticmethod
    def __find_and_return_fastest_driver_in_race(race):
        fastest_driver = None
        limit = 0
        for driver in race.drivers:
            if driver.car.speed_limit > limit:
                limit = driver.car.speed_limit
                fastest_driver = driver
        return fastest_driver

    def create_car(self, car_type: str, model: str, speed_limit: int):
        result = self.__check_if_car_exists_and_return_it(model)

        if result:
            raise Exception(f"Car {model} is already created!")

        if car_type == "SportsCar":
            self.cars.append(SportsCar(model, speed_limit))
        elif car_type == "MuscleCar":
            self.cars.append(MuscleCar(model, speed_limit))
        else:
            return
        return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        result = self.__check_if_driver_exists_and_return_it(driver_name)

        if result:
            raise Exception(f"Driver {driver_name} is already created!")

        self.drivers.append(Driver(driver_name))

        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        result = self.__check_if_race_exists_and_return_it(race_name)

        if result:
            raise Exception(f"Race {race_name} is already created!")

        self.races.append(Race(race_name))

        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__check_if_driver_exists_and_return_it(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        car = self.__find_and_return_last_car_of_given_type_if_not_taken(car_type)
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        return driver.set_car(car)

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__check_if_race_exists_and_return_it(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.__check_if_driver_exists_and_return_it(driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)

        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__check_if_race_exists_and_return_it(race_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        winners = 3
        fastest_drivers = []
        for driver in sorted(race.drivers, key=lambda x: -x.car.speed_limit):
            driver.number_of_wins += 1
            fastest_drivers.append(f"Driver {driver.name} wins the {race_name} race with a speed of "
                                   f"{driver.car.speed_limit}.")
            if len(fastest_drivers) == winners:
                break
        return '\n'.join(fastest_drivers)
