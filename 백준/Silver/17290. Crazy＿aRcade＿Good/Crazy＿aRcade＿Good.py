r, c = map(int, input().split())
r, c = r - 1, c - 1
size = 10
board = [input() for _ in range(size)]
row, col = [], [0 for _ in range(size)]
for i in range(size):
    if "o" in board[i]:
        for j in range(size):
            if board[i][j] == "o":
                col[j] = 1
    else:
        row.append(i)
mr, mc = 11, 11
for i in row:
    mr = min(mr, abs(i - r))
for i in range(size):
    if col[i] == 0:
        mc = min(mc, abs(i - c))
print(mr + mc)
