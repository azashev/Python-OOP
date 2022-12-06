# Use the following skeleton that has the structure and functionality of the classes, and test them
# Do NOT change the class
# Cover the whole class with unit tests to make sure that the class is working as intended

class Mammal:
    def __init__(self, name, mammal_type, sound):
        self.name = name
        self.type = mammal_type
        self.sound = sound
        self.__kingdom = "animals"

    def make_sound(self):
        return f"{self.name} makes {self.sound}"

    def get_kingdom(self):
        return self.__kingdom

    def info(self):
        return f"{self.name} is of type {self.type}"
