a, b, c = map(int, input().split())
a + b == c ** 2
if a == 0 or b == 0:
    print(c ** 2 - (a + b))
else:
    print(int((a + b) ** 0.5))