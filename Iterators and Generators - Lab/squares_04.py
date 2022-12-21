# Create a generator function called squares that should receive a number n.
# It should generate the squares of all numbers from 1 to n (inclusive).


def squares(n):
    value = 1

    while value <= n:
        yield value * value
        value += 1


# Test code:
print(list(squares(5)))

# Expected output:
# [1, 4, 9, 16, 25]
