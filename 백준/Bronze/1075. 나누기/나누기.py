N = int(input())
F = int(input())
for i in range(N // 100 * 100, (N // 100 + 1) * 100):
    if i % F == 0:
        print("{0:02d}".format(i % 100))
        break