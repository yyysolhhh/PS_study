A, B, C = map(int, input().split())
if 3 <= B < 6:
    r = 2
elif 6 <= B < 9:
    r = 3
elif 9 <= B < 12:
    r = 4
elif B == 12:
    r = 5
else:
    r = 1
ans = (A - 2015) * 4 + r
print(ans)