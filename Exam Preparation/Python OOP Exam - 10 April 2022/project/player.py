from project.supply.supply import Supply


class Player:
    player_names = []
    minimum_age = 12

    def __init__(self, name: str, age: int, stamina: int = 100):
        self.name = name
        self.age = age
        self.stamina = stamina
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError("Name not valid!")
        elif value in Player.player_names:
            raise Exception(f"Name {value} is already used!")
        Player.player_names.append(value)
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < Player.minimum_age:
            raise ValueError(f"The player cannot be under {Player.minimum_age} years old!")
        self.__age = value

    @property
    def stamina(self):
        return self.__stamina

    @stamina.setter
    def stamina(self, value):
        if value < 0 or value > 100:
            raise ValueError("Stamina not valid!")
        self.__stamina = value

    @property
    def need_sustenance(self):
        return self.__stamina < 100

    def _sustain_player(self, supply: Supply):
        if self.stamina + supply.energy > 100:
            self.stamina = 100
        else:
            self.stamina += supply.energy

    def __lt__(self, other):
        return self.stamina < other.stamina

    def __str__(self):
        return f"Player: {self.name}, {self.age}, {self.stamina}, {self.need_sustenance}"
