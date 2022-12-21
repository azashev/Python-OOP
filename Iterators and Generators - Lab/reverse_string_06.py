# Create a generator function called reverse_text that receives a string and yields all string characters on one line in
# reversed order.

def reverse_text(string):
    idx = 0
    n = len(string)

    while idx < n:
        yield string[n - idx - 1]
        idx += 1


# Test code:
for char in reverse_text("step"):
    print(char, end='')


# Expected output:
# pets
