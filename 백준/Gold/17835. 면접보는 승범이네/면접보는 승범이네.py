import sys
import heapq
input = sys.stdin.readline

def dijkstra():
    while pq:
        cur_c, cur_n = heapq.heappop(pq)
        if cur_c != d[cur_n]:
            continue
        for nxt_c, nxt_n in adj[cur_n]:
            if d[nxt_n] <= d[cur_n] + nxt_c:
                continue
            d[nxt_n] = d[cur_n] + nxt_c
            heapq.heappush(pq, (d[nxt_n], nxt_n))

N, M, K = map(int, input().split())
adj = [[] for _ in range(N + 1)]
for _ in range(M):
    U, V, C = map(int, input().split())
    adj[V].append((C, U))
targets = list(map(int, input().split()))
d = [sys.maxsize for _ in range(N + 1)]
pq = []
for t in targets:
    d[t] = 0
    heapq.heappush(pq, (0, t))
dijkstra()
max_cost = max(d[1:])
for i in range(1, N + 1):
    if d[i] == max_cost:
        break
print(i)
print(max_cost)