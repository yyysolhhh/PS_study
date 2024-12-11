N = int(input())
ans = 0
for a in range(2, 501):
    for b in range(a - 1, 0, -1):
        if a ** 2 - b ** 2 == N:
            ans += 1
            break
print(ans)