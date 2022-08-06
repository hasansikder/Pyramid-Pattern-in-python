n = 500
for a in range(n):
    for j in range(n - a - 1):
        print(' ', end='')
    for k in range(2 * a + 1):
        print('*', end='')
    print()