from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    needed_oxygen_units = 15

    def __init__(self, name, oxygen: int = 90):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.needed_oxygen_units
