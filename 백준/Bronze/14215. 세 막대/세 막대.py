sticks = sorted(map(int, input().split()))
l = sticks[0] + sticks[1]
if l <= sticks[2]:
    print(l + l - 1)
else:
    print(sum(sticks))