# Having the following code:
#
# def number_increment(numbers):
#
#     def increase():
#
#         # TODO: Implement
#
#     return increase()
#
#
# Complete the code, so it works as expected:
#
# Test code:
# print(number_increment([1, 2, 3]))

# Expected output:
# [2, 3, 4]


def number_increment(numbers):
    def increase():
        increased = [x + 1 for x in numbers]

        return increased

    return increase()


print(number_increment([1, 2, 3]))
