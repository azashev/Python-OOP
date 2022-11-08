from hero import Hero
from elf import Elf


# Your task is to create the following game hierarchy:
#
#
#                            Hero
#                        /     |    \
#                     Elf   Wizard Knight
#                     |        |        |
#                  MuseElf DarkWizard DarkKnight
#                              |        |
#                          SoulMaster BladeKnight
#
#
# Create separate files for each of the classes.
#
# Create a class Hero. It should contain the following attributes:
# • username: string
# • level: int
# Override the __str__() method of the base class, so it returns: "{name} of type {class_name} has level {level}"
#
#
# Test code:
hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)

#
# Expected output:
# H
# 4
# H of type Hero has level 4
# E of type Elf has level 4
# Hero
# E
# 4
