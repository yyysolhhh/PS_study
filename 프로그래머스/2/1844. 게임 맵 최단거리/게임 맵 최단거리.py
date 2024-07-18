from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
def solution(maps):
    n = len(maps[0])
    m = len(maps)
    temp_map = [[0 for _ in range(n)] for _ in range(m)]
    queue = deque([(0, 0)])
    while queue:
        y, x = queue.popleft()
        if y == m - 1 and x == n - 1:
            return temp_map[y][x] + 1
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < m and 0 <= nx < n and maps[ny][nx] == 1 and temp_map[ny][nx] == 0:
                temp_map[ny][nx] = temp_map[y][x] + 1
                queue.append((ny, nx))
    return -1