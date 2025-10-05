import sys
from heapq import heappop, heappush
input = sys.stdin.readline

def dijkstra(start, end):
    d = [sys.maxsize for _ in range(N + 1)]
    d[start] = 0
    pq = [(0, start)]
    while pq:
        cur_d, cur_n = heappop(pq)
        if cur_d != d[cur_n]:
            continue
        for nxt_d, nxt_n in adj[cur_n]:
            if d[nxt_n] <= d[cur_n] + nxt_d:
                continue
            d[nxt_n] = d[cur_n] + nxt_d
            heappush(pq, (d[nxt_n], nxt_n))
    return d[end]


N, E = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    adj[a].append((c, b))
    adj[b].append((c, a))
v1, v2 = map(int, input().split())
case1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
case2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
ans = min(case1, case2)
if ans >= sys.maxsize:
    ans = -1
print(ans)