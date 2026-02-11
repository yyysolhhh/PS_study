chess = {".": 0, "K": 0, "k": 0, "P": 1, "p": -1, "N": 3, "n": -3, "B": 3, "b": -3, "R": 5, "r": -5, "Q": 9, "q": -9}
board = [input() for _ in range(8)]
ans = 0
for row in board:
    for i in row:
        ans += chess[i]
print(ans)