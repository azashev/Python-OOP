from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    needed_oxygen_units = 5

    def __init__(self, name, oxygen: int = 70):
        super().__init__(name, oxygen)

    def breathe(self):
        self.oxygen -= self.needed_oxygen_units
