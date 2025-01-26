import sys
input = sys.stdin.readline
N, x = map(int, input().split())
poly = []
for _ in range(N + 1):
    A, i = map(int, input().split())
    poly.append(A)
ans = poly[0]
for i in range(1, N + 1):
    ans = ans * x + poly[i]
    ans %= (10 ** 9 + 7)
print(ans)