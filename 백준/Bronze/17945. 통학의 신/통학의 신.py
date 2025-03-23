A, B = map(int, input().split())
for i in range(-1000, 1001):
    if i * i + 2 * A * i + B == 0:
        print(i, end=" ")