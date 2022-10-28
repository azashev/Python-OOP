def print_row(number, n):
    print(" " * (n - number), end='')
    print("* " * number)


n = int(input())

for row in range(1, n + 1):
    print_row(row, n)

for row in range(n - 1, -1, -1):
    print_row(row, n)
