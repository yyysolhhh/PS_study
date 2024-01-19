import sys
from collections import deque, defaultdict

inputs = sys.stdin.readline

def bfs(start) -> int:
    visited = [False] * (N + 1)
    count = 0
    q = deque([start])
    visited[start] = True
    while q:
        cur = q.popleft()
        nodes = graph[cur]
        for n in nodes:
            if not visited[n]:
                q.append(n)
                visited[n] = True
                count += 1
    return count

N, M = map(int, input().split())
graph = defaultdict(list)

max_result = 0
answer = []

for _ in range(M):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, N + 1):
    current_result = bfs(i)
    if current_result > max_result:
        max_result = current_result
        answer = [i]
    elif current_result == max_result:
        answer.append(i)

print(' '.join(map(str, answer)))