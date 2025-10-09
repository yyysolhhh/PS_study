import sys
input = sys.stdin.readline
n, m = map(int, input().split())
time = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
nxt = [["-" for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    time[a][b] = min(time[a][b], t)
    time[b][a] = min(time[b][a], t)
    nxt[a][b] = b
    nxt[b][a] = a
for i in range(1, n + 1):
    time[i][i] = 0
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if time[i][j] <= time[i][k] + time[k][j]:
                continue
            time[i][j] = time[i][k] + time[k][j]
            nxt[i][j] = nxt[i][k]
for i in nxt[1:]:
    print(*i[1:])