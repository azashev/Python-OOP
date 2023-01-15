from abc import ABC, abstractmethod


class Astronaut(ABC):
    needed_oxygen_units = 10

    @abstractmethod
    def __init__(self, name: str, oxygen: int):
        self.name = name
        self.oxygen = oxygen
        self.backpack = []  # each astronaut will collect items while on a mission

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError("Astronaut name cannot be empty string or whitespace!")
        self.__name = value

    def breathe(self):
        self.oxygen -= Astronaut.needed_oxygen_units

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
