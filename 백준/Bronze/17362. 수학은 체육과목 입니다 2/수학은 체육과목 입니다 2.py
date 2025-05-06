n = int(input())
ans = n % 8
if ans > 5 or ans == 0:
    print((10 - ans) % 8)
else:
    print(ans)