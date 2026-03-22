import sys
input = sys.stdin.readline
x, y, p, a, b = map(int, input().split())
ans = 0
max_p = p + (y - 1) * b
while x > 0:
    ans += max_p
    max_p -= a
    x -= 1
print(ans)
