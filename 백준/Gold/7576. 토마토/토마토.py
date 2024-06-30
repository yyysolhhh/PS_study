from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    while (queue):
        y, x = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
                box[ny][nx] = box[y][x] + 1
                queue.append((ny, nx))
input = sys.stdin.readline
M, N = map(int, input().split())
box = []
cnt_empty = 0
res = 0
queue = deque()
for _ in range(N):
    box.append(list(map(int, input().split())))
for y, row in enumerate(box):
    for x, col in enumerate(row):
        if col == 1:
            queue.append((y, x))
        elif col == -1:
            cnt_empty += 1
if len(queue) + cnt_empty == N * M:
    print(0)
    exit(0)
bfs()
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
        res = max(res, j)
print(res - 1)