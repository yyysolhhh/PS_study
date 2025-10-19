import sys
input = sys.stdin.readline
N = int(input())
lc = [0 for _ in range(N + 1)]
rc = [0 for _ in range(N + 1)]
par = [0 for _ in range(N + 1)]
for _ in range(N):
    a, b, c = map(int, input().split())
    lc[a] = b
    rc[a] = c
    par[b] = a
    par[c] = a
K = 0
last = 1
while rc[last] != -1:
    last = rc[last]
    K += 1
print(2 * (N - 1) - K)