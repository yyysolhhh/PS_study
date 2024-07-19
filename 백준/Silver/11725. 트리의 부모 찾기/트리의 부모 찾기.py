from collections import deque
import sys
def bfs():
    queue = deque([1])
    while queue:
        curr = queue.popleft()
        for n in graph[curr]:
            if ans[n] == 0:
                ans[n] = curr
                queue.append(n)
input = sys.stdin.readline
N = int(input())
graph = [[] for _ in range(N + 1)]
ans = [0 for _ in range(N + 1)]
for _ in range(N - 1):
    p1, p2 = map(int, input().split())
    graph[p1].append(p2)
    graph[p2].append(p1)
bfs()
for i in ans[2:]:
    print(i)