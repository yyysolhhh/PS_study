import sys
from collections import deque
input = sys.stdin.readline

dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]

def bfs(x, y, num):
    cnt = 0
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        cx, cy = q.popleft()
        cnt += 1
        board[cx][cy] = num
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if visited[nx][ny] == True or board[nx][ny] > 0:
                continue
            q.append((nx, ny))
            visited[nx][ny] = True
    return cnt

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
group = [0, 0]
group_num = 2
visited = [[False for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        if board[i][j] == 0:
            group.append(bfs(i, j, group_num))
            group_num += 1
for i in range(N):
    for j in range(M):
        group_list = set()
        if board[i][j] > 1:
            print(0, end="")
        else:
            ans = 1
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if nx < 0 or nx >= N or ny < 0 or ny >= M or board[nx][ny] in group_list:
                    continue
                ans += group[board[nx][ny]]
                group_list.add(board[nx][ny])
            print(ans % 10, end="")
    print()