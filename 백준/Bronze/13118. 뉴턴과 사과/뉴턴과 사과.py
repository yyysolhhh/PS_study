p = list(map(int, input().split()))
x, y, r = map(int, input().split())
for i, j in enumerate(p, start=1):
    if j == x:
        print(i)
        break
else:
    print(0)