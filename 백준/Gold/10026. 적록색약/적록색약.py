from collections import deque
import sys
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs(i, j):
    queue = deque([(i, j)])
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and picture[ny][nx] == picture[y][x] and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = 1
input = sys.stdin.readline
N = int(input())
picture = []
for _ in range(N):
    picture.append(list(input()))
cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt, end=' ')
for i in range(N):
    for j in range(N):
        if picture[i][j] == 'G':
            picture[i][j] = 'R'
cnt = 0
visited = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j)
            cnt += 1
print(cnt)