from collections import deque
import sys
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs():
    queue = deque([(0, 0, 0)])
    visited = [[[0 for z in range(2)] for i in range(M)]
               for j in range(N)]
    w = 0
    while queue:
        y, x, w = queue.popleft()
        if y == N - 1 and x == M - 1:
            return visited[y][x][w] + 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M:
                if board[ny][nx] == 0 and visited[ny][nx][w] == 0:
                    visited[ny][nx][w] = visited[y][x][w] + 1
                    queue.append((ny, nx, w))
                elif board[ny][nx] == 1 and w == 0:
                    visited[ny][nx][w + 1] = visited[y][x][w] + 1
                    queue.append((ny, nx, w + 1))
    return -1
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(list(map(int, list(input().rstrip()))))
print(bfs())