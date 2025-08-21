N = int(input())
mon = []
for i in range(1, N + 1):
    W, H = map(int, input().split())
    ppi = ((W ** 2 + H ** 2) ** 0.5) / 77
    mon.append((i, ppi))
mon.sort(key=lambda x: (-x[1], x[0]))
for i in mon:
    print(i[0])