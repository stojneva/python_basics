n = 4

for row in range(1, n + 1):
    for col in range((n - row) * 3):
        print(' ', end='')
    print('*', end='')

    for col in range(1, (row * 2) - 1):
        print('  *', end='')
    print()

for row in range(n - 1, 0, -1):
    for col in range((n - row) * 3):
        print(' ', end='')
    print('*', end='')

    for col in range(1, (row * 2) - 1):
        print('  *', end='')
    print()