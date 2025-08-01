P = int(input())
std = {1: 0, 3: 0, 4: 0, 5: 0}
for _ in range(P):
    gp, cp, np = map(int, input().split())
    if gp == 1:
        std[5] += 1
    elif cp == 2:
        std[1] += 1
    else:
        std[cp] += 1
for i in std.values():
    print(i)