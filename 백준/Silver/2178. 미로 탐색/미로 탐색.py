import sys
from collections import deque
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs():
    queue = deque([(0, 0)])
    while queue:
        y, x = queue.popleft()
        if y == N - 1 and x == M - 1:
            return maze[y][x]
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                queue.append((ny, nx))
input = sys.stdin.readline
N, M = map(int, input().split())
maze = []
for _ in range(N):
    maze.append(list(map(int, list(input().rstrip()))))
print(bfs())