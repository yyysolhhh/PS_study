board = []
for _ in range(5):
    board.append(input())
for i in range(15):
    for j in range(5):
        if i < len(board[j]):
            print(board[j][i], end="")