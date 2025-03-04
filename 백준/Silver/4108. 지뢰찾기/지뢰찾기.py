dx = (0, 0, 1, -1, 1, -1, 1, -1)
dy = (1, -1, 0, 0, 1, -1, -1, 1)
while True:
    R, C = map(int, input().split())
    board = []
    if R == 0 and C == 0:
        break
    for _ in range(R):
        board.append(input())
    for x in range(R):
        for y in range(C):
            if board[x][y] == "*":
                print(board[x][y], end="")
                continue
            cnt = 0
            for k in range(8):
                nx, ny = x + dx[k], y + dy[k]
                if nx < 0 or ny < 0 or nx >= R or ny >= C:
                    continue
                if board[nx][ny] == "*":
                    cnt += 1
            print(cnt, end="")
        print()