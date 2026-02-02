N = int(input())
ans = 6
for i in range(11, N + 1):
    ans *= i
print(ans)