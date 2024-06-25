T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    sum_r = r1 + r2
    if r1 == r2 and d == 0:
        print(-1)
    elif abs(r1 - r2) == d or sum_r == d:
        print(1)
    elif sum_r > d and abs(r1 - r2) < d:
        print(2)
    else:
        print(0)