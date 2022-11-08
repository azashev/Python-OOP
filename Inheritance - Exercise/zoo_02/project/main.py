from mammal import Mammal
from lizard import Lizard


# Create a zoo project (separate files for each class) that contains the following classes:


#                   Animal
#                 /        \
#             Reptile     Mammal
#             /    |        |   \
#         Lizard  Snake  Gorilla Bear
#
#
# Follow the diagram and create all the classes. Except for the Animal class, each class should inherit from another
# class, as shown in the diagram. The Animal class should receive a name - string upon initialization.
# Every class should have a constructor, which accepts one parameter: name
#
#
# Test code:
mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)

#
# Expected output:
# Animal
# Stella
# Reptile
# John
