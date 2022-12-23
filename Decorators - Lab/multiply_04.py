# Having the following code:
# def multiply(times):
#
#     def decorator(function):
#
#         # TODO: Implement
#
#     return decorator
#
#
# Complete the code, so it works as expected:
#
# Test code:
# @multiply(3)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(3))
#
# Expected output:
# 39

#
# Test code:
# @multiply(5)
# def add_ten(number):
#     return number + 10
#
# print(add_ten(6))
#
# Expected output:
# 80


def multiply(times):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)

            return result * times

        return wrapper

    return decorator


@multiply(3)
def add_ten(number):
    return number + 10


print(add_ten(3))

print()


@multiply(5)
def add_ten(number):
    return number + 10


print(add_ten(6))
