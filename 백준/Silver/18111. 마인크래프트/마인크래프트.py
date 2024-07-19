N, M, B = map(int, input().split())
board = []
time = 128000000
height = 0
for _ in range(N):
    board.append(list(map(int, input().split())))
maxh = max(map(max, board))
minh = min(map(min, board))
for h in range(maxh, minh-1, -1):
    t = 0
    inventory = B
    for i in board:
        for j in i:
            gap = abs(j - h)
            if j > h:
                inventory += 1 * gap
                t += 2 * gap
            elif j < h:
                inventory -= 1 * gap
                t += 1 * gap
            else:
                continue
    if inventory < 0:
        continue
    else:
        if t < time:
            time = t
            height = h
print(time, height)