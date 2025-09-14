N = int(input())
ans = 1
for i in range(1, 10):
    porindrome = i
    while porindrome <= N:
        porindrome = porindrome * 10 + i
        ans += 1
print(ans)