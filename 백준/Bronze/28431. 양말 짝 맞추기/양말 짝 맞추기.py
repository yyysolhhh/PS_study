socks = [0 for _ in range(10)]
for _ in range(5):
    n = int(input())
    socks[n] = 1 ^ socks[n]
for i, j in enumerate(socks):
    if j:
        print(i)