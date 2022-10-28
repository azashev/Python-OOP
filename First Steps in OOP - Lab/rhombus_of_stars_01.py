def print_row(number, n):
    print(" " * (n - number), end='')
    print("* " * number)


n = int(input())

for row in range(1, n + 1):
    print_row(row, n)

for row in range(n - 1, -1, -1):
    print_row(row, n)


# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:
#
# Tests:
#
# Input:
# 1
#
# Expected output:
# *
#
#
#
# Input:
# 2
#
# Expected output:
#  *
# * *
#  *
#
#
#
# Input:
# 3
#
# Expected output:
#   *
#  * *
# * * *
#  * *
#   *
#
#
#
# Input:
# 4
#
# Expected output:
#    *
#   * *
#  * * *
# * * * *
#  * * *
#   * *
#    *
