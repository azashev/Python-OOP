from abc import abstractmethod, ABC


class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


class Cat(Animal):
    def make_sound(self):
        return "meow"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof"


animals = [Cat(), Dog()]
animal_sound(animals)

# Refactor the provided code below, so you do not need to make any changes in it when you want to add new species to the
# animals list
#
#
# Code to refactor:
#
# class Animal:
#     def __init__(self, species):
#         self.species = species
#
#     def get_species(self):
#         return self.species
#
#
# def animal_sound(animals: list):
#     for animal in animals:
#         if animal.species == 'cat':
#             print('meow')
#         elif animal.species == 'dog':
#             print('woof-woof')
#
#
# animals = [Animal('cat'), Animal('dog')]
# animal_sound(animals)
