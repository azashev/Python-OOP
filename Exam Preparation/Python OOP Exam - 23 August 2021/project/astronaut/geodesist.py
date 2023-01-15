from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    def __init__(self, name, oxygen: int = 50):
        super().__init__(name, oxygen)
