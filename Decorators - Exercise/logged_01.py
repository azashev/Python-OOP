# Create a decorator called logged. It should return the name of the function that is being called and its parameters.
# It should also return the result of the execution of the function being called.


def logged(function):
    def wrapper(*args):
        return f"you called {function.__name__}({', '.join(str(x) for x in args)})\nit returned {function(*args)}"

    return wrapper


# Test code:
@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


# Expected result:
# you called func(4, 4, 4)
# it returned 6


print()


# Test code:
@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))

# Expected result:
# you called sum_func(1, 4)
# it returned 5
