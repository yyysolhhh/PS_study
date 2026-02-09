a, b = map(int, input().split())
col = abs((b - 1) // 4 - (a - 1) // 4)
row = abs((b - 1) % 4 - (a - 1) % 4)
print(col + row)