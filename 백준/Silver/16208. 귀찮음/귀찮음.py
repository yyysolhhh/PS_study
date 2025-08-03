n = int(input())
a = list(map(int, input().split()))
ans = 0
total = sum(a)
for i in range(n - 1):
    ans += a[i] * (total - a[i])
    total -= a[i]
print(ans)