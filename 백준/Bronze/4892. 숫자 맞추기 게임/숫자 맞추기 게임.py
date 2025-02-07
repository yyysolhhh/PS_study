i = 1
while True:
    n = int(input())
    if n == 0:
        break
    n4 = n // 2 if n % 2 == 0 else (n - 1) // 2
    print(f"{i}. {"odd" if n % 2 == 1 else "even"} {n4}")
    i += 1