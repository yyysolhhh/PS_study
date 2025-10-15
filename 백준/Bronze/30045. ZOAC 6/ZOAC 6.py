N = int(input())
ans = 0
for _ in range(N):
    S = input()
    if "01" in S or "OI" in S:
        ans += 1
print(ans)
