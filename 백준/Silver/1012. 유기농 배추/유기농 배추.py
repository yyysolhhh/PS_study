from collections import deque
import sys

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def bfs():
    while (queue):
        y, x = queue.popleft()
        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]
            if 0 <= ny < N and 0 <= nx < M and field[ny][nx] == 1:
                queue.append((ny, nx))
                field[ny][nx] = -1


input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    cnt = 0
    for _ in range(K):
        X, Y = map(int, input().split())
        field[Y][X] = 1
    for row, line in enumerate(field):
        for col, val in enumerate(line):
            if val == 1:
                queue.append((row, col))
                bfs()
                cnt += 1
    print(cnt)