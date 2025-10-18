import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    q = deque([start])
    while q:
        cur = q.popleft()
        for nxt in graph[cur]:
            if parent[cur] == nxt:
                continue
            if parent[nxt]:
                return 0
            parent[nxt] = cur
            q.append(nxt)
    return 1

t = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    graph = [[] for _ in range(n + 1)]
    parent = [0 for _ in range(n + 1)]
    ans = 0
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    for i in range(1, n + 1):
        if parent[i] == 0:
            ans += bfs(i)
    print(f"Case {t}:", end=" ")
    if ans == 0:
        print("No trees.")
    elif ans == 1:
        print("There is one tree.")
    else:
        print(f"A forest of {ans} trees.")
    t += 1