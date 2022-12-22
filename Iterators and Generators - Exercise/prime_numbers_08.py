# Create a generator function called get_primes() which should receive a list of integer numbers and return a list
# containing only the prime numbers from the initial list.

def get_primes(numbers):
    for number in numbers:
        if number <= 1:
            continue

        for num in range(2, number):
            if number % num == 0:
                break
        else:
            yield number


# Test code:

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

# Expected output:
# [2, 3, 5]


print()


# Test code:

print(list(get_primes([-2, 0, 0, 1, 1, 0])))

# Expected output:
# []
