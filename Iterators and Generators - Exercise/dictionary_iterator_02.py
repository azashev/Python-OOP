# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object.
# Implement the iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the
# value).

class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.items = list(dictionary.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.items):
            raise StopIteration

        result_to_return = self.items[self.idx]
        self.idx += 1

        return result_to_return


# Test code:

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

# Expected output:
# (1, '1')
# (2, '2')


print()


# Test code:

result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)

# Expected output:
# ('name', 'Peter')
# ('age', 24)
