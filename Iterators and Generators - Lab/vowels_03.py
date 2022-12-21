# Create a class called vowels, which should receive a string.
# Implement the __iter__ and __next__ methods, so the iterator returns only the vowels from the string.


class vowels:
    vowel_chars = 'eyuioa'

    def __init__(self, text):
        self.text = text
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.idx < len(self.text):
            if self.text[self.idx].lower() not in self.vowel_chars:
                self.idx += 1
                continue

            value = self.text[self.idx]
            self.idx += 1

            return value

        raise StopIteration


# Test code:
my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)


# Expected output:
# A
# e
# i
# u
# y
# o
