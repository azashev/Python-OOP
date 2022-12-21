# Create a class called reverse_iter which should receive an iterable upon initialization.
# Implement the __iter__ and __next__ methods, so the iterator returns the items of the iterable in reversed order.


class reverse_iter:
    def __init__(self, values):
        self.values = list(values)
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < -len(self.values):
            raise StopIteration

        value = self.values[self.idx]
        self.idx -= 1

        return value


# Test code:
reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)

# Expected output:
# 4
# 3
# 2
# 1
