a, b = map(int, input().split())
if a & 1 and b & 1:
    print(min(a, b))
else:
    print(0)