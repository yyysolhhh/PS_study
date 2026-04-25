N, M = map(int, input().split())
ans = N // M
if N % M > 0:
    ans += 1
print(ans)
