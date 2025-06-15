R, C = map(int, input().split())
board = []
for i in range(R):
    line = input()
    board.append(line)
    board[i] += line[::-1]
A, B = map(int, input().split())
A, B = A - 1, B - 1
for i in board[::-1]:
    board.append(i)
board[A] = list(board[A])
if board[A][B] == "#":
    board[A][B] = "."
else:
    board[A][B] = "#"
board[A] = "".join(board[A])
for l in board:
    print(l)