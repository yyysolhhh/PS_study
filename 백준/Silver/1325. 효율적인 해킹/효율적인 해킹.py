import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    visited = [0 for _ in range(N + 1)]
    visited[s] = 1
    while q:
        cur = q.popleft()
        for i in rel[cur]:
            if visited[i]:
                continue
            visited[i] = 1
            q.append(i)
    return sum(visited)


N, M = map(int, input().split())
rel = [[] for _ in range(N + 1)]
res = []
for _ in range(M):
    A, B = map(int, input().split())
    rel[B].append(A)
for i in range(1, N + 1):
    res.append(bfs(i))
ans = []
for i in range(N):
    if res[i] == max(res):
        ans.append(i + 1)
print(*ans)