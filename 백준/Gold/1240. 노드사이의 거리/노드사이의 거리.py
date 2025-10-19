import sys
from collections import deque
input = sys.stdin.readline

def solve(st, en):
    visited = [0 for _ in range(N + 1)]
    q = deque([st])
    visited[st] = 0
    while q:
        cur = q.pop()
        if cur == en:
            return visited[en]
        for nxt, dist in graph[cur]:
            if visited[nxt] > 0:
                continue
            visited[nxt] = visited[cur] + dist
            q.append(nxt)

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    u, v, c = map(int, input().split())
    graph[u].append((v, c))
    graph[v].append((u, c))
for _ in range(M):
    u, v = map(int, input().split())
    print(solve(u, v))