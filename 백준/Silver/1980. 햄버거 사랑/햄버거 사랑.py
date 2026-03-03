n, m, t = map(int, input().split())
cola = t
cnt = 0
for tow in range(t // n, -1, -1):
    for bul in range(t // m, -1, -1):
        tmp = tow * n + bul * m
        if t >= tmp:
            if t - tmp < cola:
                    cnt = tow + bul
                    cola = t - tmp
            elif t - tmp == cola:
                if cnt < tow + bul:
                    cnt = tow + bul
                    cola = t - tmp
print(cnt, cola)
