import sys
from heapq import heappush, heappop
input = sys.stdin.readline

N, M, K = map(int, input().split())
d = [[sys.maxsize for _ in range(N + 1)] for _ in range(K + 1)]
adj = [[] for _ in range(N + 1)]
# time, k, city
for _ in range(M):
    s, e, t = map(int, input().split())
    adj[s].append((t, 0, e))
    adj[e].append((t, 0, s))
    adj[s].append((0, 1, e))
    adj[e].append((0, 1, s))
for i in range(0, K + 1):
    d[i][1] = 0
pq = [(0, 0, 1)]
while pq:
    cur_t, cur_k, cur_n = heappop(pq);
    if cur_t != d[cur_k][cur_n]:
        continue
    for nxt_t, nxt_k, nxt_n in adj[cur_n]:
        nxt_t += cur_t
        nxt_k += cur_k
        if nxt_k > K:
            continue
        if d[nxt_k][nxt_n] <= nxt_t:
            continue
        d[nxt_k][nxt_n] = nxt_t
        heappush(pq, (nxt_t, nxt_k, nxt_n))
ans = sys.maxsize
for i in range(len(d)):
    ans = min(ans, d[i][N])
print(ans)