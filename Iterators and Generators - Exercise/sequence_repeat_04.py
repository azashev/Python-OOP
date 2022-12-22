# Create a class called sequence_repeat which should receive a sequence and a number upon initialization.
# Implement an iterator to return the given elements, so they form a string with a length - the given number.
# If the number is greater than the number of elements, then the sequence repeats as necessary.

class sequence_repeat:
    def __init__(self, seq: str, num: int):
        self.seq = seq
        self.num = num
        self.idx = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx == self.num - 1:
            raise StopIteration

        self.idx += 1

        return self.seq[self.idx % len(self.seq)]


# Test code:

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')

# Expected output:
# abcab


print()


# Test code:

result = sequence_repeat('I Love Python', 3)
for item in result:
    print(item, end='')

# Expected output:
# I L
