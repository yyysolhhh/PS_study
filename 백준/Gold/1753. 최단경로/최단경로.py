import sys
import heapq
input = sys.stdin.readline
V, E = map(int, input().split())
K = int(input())
d = [sys.maxsize for _ in range(V + 1)]
adj = [[] for _ in range(V + 1)]
pq = []
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))
d[K] = 0
heapq.heappush(pq, (d[K], K))
while pq:
    cur_d, cur_n = heapq.heappop(pq)
    if d[cur_n] != cur_d:
        continue
    for nxt_d, nxt_n in adj[cur_n]:
        if d[nxt_n] <= d[cur_n] + nxt_d:
            continue
        d[nxt_n] = d[cur_n] + nxt_d
        heapq.heappush(pq, (d[nxt_n], nxt_n))
for i in d[1:]:
    if i == sys.maxsize:
        print("INF")
    else:
        print(i)