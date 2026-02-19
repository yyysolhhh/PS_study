R, C = map(int, input().split())
Rg, Cg, Rp, Cp = map(int, input().split())
board = [input() for _ in range(R)]
cnt = 0
for i in board:
    cnt += i.count("P")
if cnt == Rp * Cp:
    print(0)
else:
    print(1)