# Create a decorator function called even_parameters.
# It should check if all parameters passed to a function are even numbers and only then execute the function and return
# the result. Otherwise, don't execute the function and return "Please use only even numbers!"


def even_parameters(func):
    def wrapper(*args):
        for arg in args:
            if isinstance(arg, int):
                if arg % 2 == 0:
                    continue
            return "Please use only even numbers!"
        return func(*args)
    return wrapper


# Test code:
@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

# Expected result:
#


print()


# Test code:
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

# Expect result:
# 384
# Please use only even numbers!
