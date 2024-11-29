A, B = map(int, input().split())
ans = 1
for i in range(1, B + 1):
    ans = ans + (A - 2) * i + 1
print(ans)