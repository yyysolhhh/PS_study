from heapq import heappush, heappop
N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    indegree[B] += 1
q = []
for i in range(1, N + 1):
    if indegree[i] == 0:
        heappush(q, i)
while q:
    cur = heappop(q)
    print(cur, end=" ")
    for nxt in adj[cur]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heappush(q, nxt)