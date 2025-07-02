N, m, M, T, R = map(int, input().split())
ans, n = 0, 0
cur = m
if m + T > M:
    ans = -1
else:
    while n < N:
        if cur + T > M:
            cur -= R
            if cur < m:
                cur = m
        else:
            cur += T
            n += 1
        ans += 1
print(ans)
