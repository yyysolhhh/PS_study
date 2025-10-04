import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def dijkstra(s):
    pq = [(0, s)]
    heappush(pq, (0, s))
    while pq:
        cur_d, cur_n = heappop(pq)
        if d[cur_n] != cur_d:
            continue
        for nxt_d, nxt_n in adj[cur_n]:
            if d[nxt_n] <= d[cur_n] + nxt_d:
                continue
            d[nxt_n] = d[cur_n] + nxt_d
            heappush(pq, (d[nxt_n], nxt_n))

N = int(input())
M = int(input())
adj = [[] for _ in range(N + 1)]
d = [sys.maxsize for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    adj[start].append((cost, end))
s, e = map(int, input().split())
d[s] = 0
dijkstra(s)
print(d[e])