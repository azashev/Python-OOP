# Test the provided skeleton:

class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


# Description
#
# Create the following tests:
# • Cat's size is increased after eating
# • Cat is fed after eating
# • Cat cannot eat if already fed, raises an error
# • Cat cannot fall asleep if not fed, raises an error
# • Cat is not sleepy after sleeping
