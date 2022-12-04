from project.cat import Cat


class Kitten(Cat):
    GENDER = "Female"

    def __init__(self, name: str, age: int):
        super().__init__(name, age, gender=Kitten.GENDER)

    def make_sound(self):
        return "Meow"