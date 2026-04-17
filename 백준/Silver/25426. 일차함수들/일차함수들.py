import sys
input = sys.stdin.readline
N = int(input())
ab = []
ans = 0
for _ in range(N):
    ab.append(list(map(int, input().split())))
ab.sort()
for n, x in zip(ab, range(1, N + 1)):
    ans += n[0] * x + n[1]
print(ans)
