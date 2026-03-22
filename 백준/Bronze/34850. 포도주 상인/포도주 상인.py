x, y, p, a, b = map(int, input().split())
ans = 0
if b > 0:
    max_p = p + (y - 1) * b
else:
    max_p = p
while x > 0:
    ans += max_p
    max_p -= a
    x -= 1
print(ans)
