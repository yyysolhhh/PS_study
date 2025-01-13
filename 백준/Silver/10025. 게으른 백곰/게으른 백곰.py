import sys
input = sys.stdin.readline
MAX = 1_000_001
N, K = map(int, input().split())
ice = [0 for _ in range(MAX)]
for _ in range(N):
    g, x = map(int, input().split())
    ice[x] = g
size = 2 * K + 1
window = sum(ice[:size])
ans = window
for i in range(size, MAX):
    window += ice[i] - ice[i - size]
    ans = max(ans, window)
print(ans)