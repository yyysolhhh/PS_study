H, W, N, M = map(int, input().split())
row, col = 0, 0
for i in range(0, H, N + 1):
    row += 1
for i in range(0, W, M + 1):
    col += 1
print(row * col)
