# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int).
# Implement the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the
# given step.

class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.iterations = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.iterations == self.count - 1:
            raise StopIteration

        self.iterations += 1

        return self.iterations * self.step


# Test code:

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

# Expected output:
# 0
# 2
# 4
# 6
# 8
# 10


print()


# Test code:

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

# Expected output:
# 0
# 10
# 20
# 30
# 40
