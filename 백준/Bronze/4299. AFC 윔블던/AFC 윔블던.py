tot, diff = map(int, input().split())
if tot + diff < 0 or tot - diff < 0 or (tot + diff) % 2:
    print(-1)
else:
    a = (tot + diff) // 2
    b = tot - a
    print(a, b)