n = int(input())
ans = 1
if n < 5:
    for i in range(2, n + 1):
        ans *= i
    print(ans % 10)
else:
    print(0)