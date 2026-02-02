N = int(input())
fac = 1
for i in range(2, N + 1):
    fac *= i
ans = fac // 60 // 60 // 24 // 7
print(ans)