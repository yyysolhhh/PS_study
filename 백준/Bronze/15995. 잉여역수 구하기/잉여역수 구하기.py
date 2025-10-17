a, m = map(int, input().split())
i = 1
while True:
    if a * i % m == 1:
        print(i)
        break
    i += 1