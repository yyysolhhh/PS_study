import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
deg = [0 for _ in range(N + 1)]
for _ in range(M):
    inp = list(map(int, input().split()))
    for i in range(1, inp[0]):
        adj[inp[i]].append(inp[i + 1])
        deg[inp[i + 1]] += 1
q = deque()
for i in range(1, N + 1):
    if deg[i] == 0:
        q.append(i)
result = []
while q:
    cur = q.popleft()
    result.append(cur)
    for i in adj[cur]:
        deg[i] -= 1
        if deg[i] == 0:
            q.append(i)
if len(result) != N:
    print(0)
else:
    for i in result:
        print(i)