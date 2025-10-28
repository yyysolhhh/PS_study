import sys
from collections import deque
input = sys.stdin.readline

def bfs(node):
    if parents[node] == -1:
        return 0
    ans = len(leaf)
    if node in leaf:
        ans -= 1
    q = deque([node])
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            if nxt in leaf:
                ans -= 1
            q.append(nxt)
    if len(adj[parents[node]]) == 1:
        ans += 1
    return ans

N = int(input())
parents = list(map(int, input().split()))
erase = int(input())
adj = [[] for _ in range(N)]
outdegree = [0 for _ in range(N)]
for i in range(N):
    if parents[i] == -1:
        continue
    adj[parents[i]].append(i)
    outdegree[parents[i]] += 1
leaf = []
for i in range(N):
    if outdegree[i] == 0:
        leaf.append(i)
print(bfs(erase))