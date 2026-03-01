n = int(input())
n5, n2 = n // 5, 0
while True:
    n2 = (n - 5 * n5) // 2
    if 5 * n5 + 2 * n2 == n:
        print(n2 + n5)
        break
    n5 -= 1
    if n5 < 0:
        print(-1)
        break