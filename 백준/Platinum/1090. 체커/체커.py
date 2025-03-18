N = int(input())
x = []
y = []
ans = [1000000000 for _ in range(N)]
for _ in range(N):
    tmp_x, tmp_y = list(map(int, input().split()))
    x.append(tmp_x)
    y.append(tmp_y)
for i in x:
    for j in y:
        dist = []
        for k in range(N):
            dist.append(abs(x[k] - i) + abs(y[k] - j))
        dist.sort()
        for k in range(N):
            ans[k] = min(ans[k], sum(dist[:k + 1]))
print(*ans)