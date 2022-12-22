def solution():
    def integers():
        num = 1
        
        while True:
            yield num
            num += 1

    def halves():
        for num in integers():
            yield num / 2

    def take(n, seq):
        return [next(seq) for _ in range(n)]

    return take, halves, integers


# You are given a skeleton with the following code:
#
# def solution():
#
#     def integers():
#         TODO: Implement
#
#     def halves():
#
#         for i in integers():
#             TODO: Implement
#
#     def take(n, seq):
#         TODO: Implement
#
#     return (take, halves, integers)
#
#
# Implement the following functions:
# • integers() - generates an infinite amount of integers (starting from 1)
# • halves() -  generates the halves of those integers (each integer / 2)
# • take(n, seq) - takes the first n halves of those integers
#
#
# Test code:
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))

# Expected output:
# [0.5, 1.0, 1.5, 2.0, 2.5]


print()


# Test code:

take = solution()[0]
halves = solution()[1]
print(take(0, halves()))

# Expected output:
# []
