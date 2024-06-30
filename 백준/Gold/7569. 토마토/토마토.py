from collections import deque
import sys

dx, dy, dh = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
def bfs():
    while queue:
        h, y, x = queue.popleft()
        for i in range(6):
            nh = h + dh[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M and box[nh][ny][nx] == 0:
                box[nh][ny][nx] = box[h][y][x] + 1
                queue.append((nh, ny, nx))
                
input = sys.stdin.readline
M, N, H = map(int, input().split())
box = [[] for _ in range(H)]
queue = deque()
res = 0
for h in range(H):
    for y in range(N):
        box[h].append(list(map(int, input().split())))
        for x in range(M):
            if box[h][y][x] == 1:
                queue.append((h, y, x))
bfs()
for h in box:
    for y in h:
        for x in y:
            if x == 0:
                print(-1)
                exit()
            else:
                res = max(res, x)
print(res - 1)