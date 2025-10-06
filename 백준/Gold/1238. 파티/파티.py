import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N, M, X = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    s, e, t = map(int, input().split())
    adj[s].append((t, e))

def dijkstra(start, end):
    d = [sys.maxsize for _ in range(N + 1)]
    d[start] = 0
    pq = [(0, start)]
    while pq:
        cur_t, cur_n = heappop(pq)
        if cur_t != d[cur_n]:
            continue
        for nxt_t, nxt_n in adj[cur_n]:
            if d[nxt_n] <= d[cur_n] + nxt_t:
                continue
            d[nxt_n] = d[cur_n] + nxt_t
            heappush(pq, (d[nxt_n], nxt_n))
    return d[end]

students = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    students[i] = dijkstra(i, X) + dijkstra(X, i)
print(max(students))