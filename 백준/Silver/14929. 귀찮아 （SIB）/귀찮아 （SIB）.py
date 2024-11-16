n = int(input())
x = list(map(int, input().split()))
ans = 0
xsum = 0
for i in range(n - 1, 0, -1):
    xsum += x[i]
    ans += xsum * x[i - 1]
print(ans)