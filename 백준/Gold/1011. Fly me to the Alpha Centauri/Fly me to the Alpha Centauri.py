T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    distance = y - x
    rep = 0
    while distance > rep * (rep + 1):
        rep += 1
    if distance <= rep ** 2:
        print(2 * rep - 1)
    else:
        print(2 * rep)
