import sys
input = sys.stdin.readline

def check_y(cur_y, n):
    for i in range(9):
        if board[cur_y][i] == n:
            return False
    return True
        
def check_x(cur_x, n):
    for i in range(9):
        if board[i][cur_x] == n:
            return False
    return True

def check_area(cur_y, cur_x, n):
    y = cur_y // 3 * 3
    x = cur_x // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[y + i][x + j] == n:
                return False
    return True
        

def backtracking(depth):
    if depth >= len(points):
        for line in board:
            print("".join(map(str, line)))
        exit()
    cur_y, cur_x = points[depth]
    for i in range(1, 10):
        if not check_y(cur_y, i) or not check_x(cur_x, i) or not check_area(cur_y, cur_x, i):
            continue
        board[cur_y][cur_x] = i
        backtracking(depth + 1)
        board[cur_y][cur_x] = 0


board = []
points = []
for i in range(9):
    board.append(list(map(int, input().strip())))
    for j in range(9):
        if board[i][j] == 0:
            points.append((i, j))
backtracking(0)