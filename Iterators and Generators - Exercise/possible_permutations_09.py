# Create a generator function called possible_permutations() which should receive a list and return lists with all
# possible permutations between its elements.

from itertools import permutations


def possible_permutations(seq):
    for el in permutations(seq):
        yield list(el)


# Test code:

[print(n) for n in possible_permutations([1, 2, 3])]

# Expected output:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]


print()


# Test code:

[print(n) for n in possible_permutations([1])]

# Expected output:
# [1]
