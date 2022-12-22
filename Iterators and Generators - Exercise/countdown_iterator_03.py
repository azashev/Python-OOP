# Create a class called countdown_iterator. Upon initialization, it should receive a count.
# Implement the iterator to return each countdown number (from count to 0 inclusive), separated by a single space.

class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.number = count + 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        self.number -= 1

        return self.number


# Test code:

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

# Expected output:
# 10 9 8 7 6 5 4 3 2 1 0


print()


# Test code:

iterator = countdown_iterator(0)
for item in iterator:
    print(item, end=" ")

# Expected output:
# 0
