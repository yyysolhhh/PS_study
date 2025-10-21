import sys
input = sys.stdin.readline
N = int(input())
coord = []
for _ in range(N):
    x, y = map(int, input().split())
    coord.append((x, y))
coord.append(coord[0])
ans = 0
for i in range(N):
    ans += coord[i][0] * coord[i + 1][1] - coord[i + 1][0] * coord[i][1]
ans = abs(ans) * 0.5
print(round(ans, 1))