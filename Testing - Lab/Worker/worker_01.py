# Test the provided skeleton:

class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


# Description
#
# Create a class WorkerTests in new project Tests.
# Create the following tests:
# • Test if the worker is initialized with the correct name, salary, and energy
# • Test if the worker's energy is incremented after the rest method is called
# • Test if an error is raised if the worker tries to work with negative energy or equal to 0
# • Test if the worker's money is increased by his salary correctly after the work method is called
# • Test if the worker's energy is decreased after the work method is called
# • Test if the get_info method returns the proper string with correct values
