N = int(input())
res = list(map(int, input().split()))
ans = 0
plus = 0
for i, j in enumerate(res):
    if j == 0:
        plus = 0
    plus += j
    ans += plus
print(ans)