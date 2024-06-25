from collections import deque
import copy
import sys
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def bfs():
    global max_safe
    queue = origin_queue.copy()
    temp_lab = copy.deepcopy(lab)
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and temp_lab[ny][nx] == 0:
                temp_lab[ny][nx] = 2
                queue.append((ny, nx))
    max_safe = max(max_safe, safe_area(temp_lab))
def set_wall(cnt, prev_i):
    if cnt == 3:
        bfs()
        return
    for i in range(prev_i, N):
        for j in range(M):
            if lab[i][j] == 0:
                lab[i][j] = 1
                set_wall(cnt + 1, i)
                lab[i][j] = 0
def safe_area(lab):
    cnt = 0
    for i in lab:
        cnt += i.count(0)
    return (cnt)
input = sys.stdin.readline
N, M = map(int, input().split())
lab = []
origin_queue = deque()
max_safe = 0
for _ in range(N):
    lab.append(list(map(int, input().split())))
for i, row in enumerate(lab):
    for j, col in enumerate(row):
        if col == 2:
            origin_queue.append((i, j))
set_wall(0, 0)
print(max_safe)