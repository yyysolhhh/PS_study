import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
relation = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, input().split())
    relation[x].append(y)
    relation[y].append(x)
deq = deque()
visited = [-1 for _ in range(n + 1)]
deq.append(p1)
visited[p1] = 0
while deq:
    cur = deq.pop()
    for i in relation[cur]:
        if visited[i] >= 0:
            continue
        deq.append(i)
        visited[i] = visited[cur] + 1
print(visited[p2])