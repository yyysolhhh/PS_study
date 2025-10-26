import sys
from collections import deque
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    D = list(map(int, input().split()))
    adj = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    for _ in range(K):
        X, Y = map(int, input().split())
        adj[X].append(Y)
        indegree[Y] += 1
    W = int(input())
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
    time = [0 for _ in range(N + 1)]
    while q:
        cur = q.popleft()
        for nxt in adj[cur]:
            time[nxt] = max(D[cur - 1] + time[cur], time[nxt])
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                q.append(nxt)
    print(time[W] + D[W - 1])