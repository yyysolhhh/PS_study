def recursive(n, i, j):
    if n == 3:
        board[i][j] = '*'
        board[i + 1][j - 1] = board[i + 1][j + 1] = '*'
        board[i + 2][j - 2:j + 3] = ["*" for _ in range(5)]
        return
    n //= 2
    recursive(n, i, j)
    recursive(n, i + n, j - n)
    recursive(n, i + n, j + n)
N = int(input())
board = [[' ' for _ in range(N * 2 - 1)] for _ in range(N)]
recursive(N, 0, N - 1)
for i in board:
    print(''.join(i))