from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    completed_missions = 0
    failed_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()     # a new repository created for each space station
        self.astronaut_repository = AstronautRepository()      # a new repository created for each space station

    def _check_if_astronaut_with_given_name_exists_and_return_it(self, astronaut_name: str):
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.name == astronaut_name:
                return astronaut

    def _check_if_planet_with_given_name_exists_and_return_it(self, planet_name: str):
        for planet in self.planet_repository.planets:
            if planet.name == planet_name:
                return planet

    def add_astronaut(self, astronaut_type: str, name: str):
        if self._check_if_astronaut_with_given_name_exists_and_return_it(name):
            return f"{name} is already added."

        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        if astronaut_type == "Biologist":
            new_astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            new_astronaut = Geodesist(name)
        else:
            new_astronaut = Meteorologist(name)
        self.astronaut_repository.add(new_astronaut)

        return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name: str, items: str):
        if self._check_if_planet_with_given_name_exists_and_return_it(name):
            return f"{name} is already added."

        new_planet = Planet(name)
        new_planet.items = items.split(', ')
        self.planet_repository.add(new_planet)

        return f"Successfully added Planet: {name}."

    def retire_astronaut(self, name: str):
        astronaut = self._check_if_astronaut_with_given_name_exists_and_return_it(name)

        if not astronaut:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.remove(astronaut)

        return f"Astronaut {name} was retired!"

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self._check_if_planet_with_given_name_exists_and_return_it(planet_name)

        if not planet:
            raise Exception("Invalid planet name!")

        astronaut_participants = []

        for astronaut in sorted(self.astronaut_repository.astronauts, key=lambda x: -x.oxygen):
            if astronaut.oxygen > 30:
                astronaut_participants.append(astronaut)

        astronaut_participants = astronaut_participants[0:5]

        if not astronaut_participants:
            raise Exception("You need at least one astronaut to explore the planet!")

        astronauts_gone_out = 0
        is_successful = False
        for astronaut in astronaut_participants:
            if not planet.items:
                break
            while astronaut.oxygen > 0 and planet.items:
                astronaut.backpack.append(planet.items.pop())
                astronaut.breathe()
            astronauts_gone_out += 1

        if not planet.items:
            is_successful = True

        if is_successful:
            SpaceStation.completed_missions += 1
            return f"Planet: {planet_name} was explored. {astronauts_gone_out} astronauts participated in collecting " \
                   f"items."
        else:
            SpaceStation.failed_missions += 1
            return "Mission is not completed."

    def report(self):
        result = [f"{SpaceStation.completed_missions} successful missions!",
                  f"{SpaceStation.failed_missions} missions were not completed!", "Astronauts' info:"]

        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.backpack:
                backpack_items = ', '.join(astronaut.backpack)
            else:
                backpack_items = "none"

            result.append(f"Name: {astronaut.name}\n"
                          f"Oxygen: {astronaut.oxygen}\n"
                          f"Backpack items: {backpack_items}")

        return '\n'.join(result)
