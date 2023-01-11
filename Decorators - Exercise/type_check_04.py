# Create a decorator called type_check. It should receive a type (int/float/str/…), and it should check if the parameter
# passed to the decorated function is of the type given to the decorator.
# If it is, execute the function and return the result, otherwise return "Bad Type".


def type_check(expected_type):
    def decorator(func):
        def wrapper(arg):
            if not isinstance(arg, expected_type):
                return "Bad Type"
            return func(arg)

        return wrapper

    return decorator


# Test code:
@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))

# Expected output:
# 4
# Bad Type


print()


# Test code:
@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))

# Expected output:
# H
# Bad Type
