from project.animals.animal import Bird
from project.food import Vegetable, Fruit, Meat, Seed


class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def type_of_food(self):
        return [Meat]

    @property
    def gained_weight(self):
        return 0.25

    def make_sound(self):
        return "Hoot Hoot"


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float):
        super().__init__(name, weight, wing_size)

    @property
    def type_of_food(self):
        return [Vegetable, Fruit, Meat, Seed]

    @property
    def gained_weight(self):
        return 0.35

    def make_sound(self):
        return "Cluck"
