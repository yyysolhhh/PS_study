import sys
input = sys.stdin.readline
def to_abs(x, y):
    if x - y >= 0:
        return x - y
    else:
        return y - x
def is_duplicated(col):
    for i in range(col):
        if board[i] == board[col]:
            return 1
        if to_abs(board[i], board[col]) == to_abs(i, col):
            return 1
    return 0
def solve(col):
    global cnt
    row = 0
    if col == N:
        cnt += 1
        return
    while row < N:
        board[col] = row
        if (is_duplicated(col) == 0):
            solve(col + 1)
        row += 1
N = int(input())
board = [0 for _ in range(N)]
cnt = 0
solve(0)
print(cnt)