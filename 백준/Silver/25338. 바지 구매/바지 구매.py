import sys
input = sys.stdin.readline
a, b, c, d = map(int, input().split())
N = int(input())
ans = 0
for _ in range(N):
    u, v = map(int, input().split())
    if v >= b and u == max(a * (v - b) ** 2 + c, d):
        ans += 1
print(ans)