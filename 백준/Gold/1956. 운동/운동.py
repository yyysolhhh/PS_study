import sys
input = sys.stdin.readline
V, E = map(int, input().split())
dist = [[sys.maxsize for _ in range(V + 1)] for _ in range(V + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    dist[a][b] = min(dist[a][b], c)
for k in range(1, V + 1):
    for i in range(1, V + 1):
        for j in range(1, V + 1):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
cycle = sys.maxsize
for i in range(1, V + 1):
    cycle = min(cycle, dist[i][i])
print(cycle if cycle < sys.maxsize else -1)