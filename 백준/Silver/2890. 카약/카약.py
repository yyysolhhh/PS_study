import sys
input = sys.stdin.readline
R, C = map(int, input().split())
board = []
rank = [0 for _ in range(10)]
for _ in range(R):
    board.append(input())
r = 1
flag = 0
for i in range(C - 2, 0, -1):
    for j in range(R):
        if board[j][i].isdigit() and rank[int(board[j][i])] == 0:
            rank[int(board[j][i])] = r
            flag = 1
    if flag:
        r += 1
        flag = 0
for i in rank[1:]:
    print(i)