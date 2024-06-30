T = int(input())
for _ in range(T):
    result = -1

    M, N, x, y = map(int, input().split())
    while x <= M * N:
        if (x - y) % N == 0:
            result = x
            break
        x += M
    print(result)
