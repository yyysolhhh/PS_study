side = sorted(map(int, input().split()))
if side[0] == side[1] == side[2]:
    print(2)
elif side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
    print(1)
else:
    print(0)