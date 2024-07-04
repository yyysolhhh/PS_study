from collections import deque
import sys

def bfs(N):
    queue = deque([N])
    while (queue):
        curr = queue.popleft()
        if curr == K:
            return (visited[curr])
        for i in (curr - 1, curr + 1, curr * 2):
            if 0 <= i <= max and not visited[i]:
                visited[i] = visited[curr] + 1
                queue.append(i)
                
input = sys.stdin.readline
N, K = map(int, input().split())
max = 10 ** 5
visited = [0 for _ in range(max + 1)]

print(bfs(N))