import sys
from collections import deque
input = sys.stdin.readline

def bfs(s, visited):
    q = deque([s])
    visited[s] = 1
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if visited[i] == visited[cur]:
                return False
            if visited[i] != 0:
                continue
            visited[i] = -1 if visited[cur] == 1 else 1
            q.append(i)
    return True

def is_bipartite_graph():
    visited = [0 for _ in range(V + 1)]
    for i in range(1, V + 1):
        if visited[i] == 0:
            if not bfs(i, visited):
                return False
    return True

K = int(input())
for _ in range(K):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    if is_bipartite_graph():
        print("YES")
    else:
        print("NO")