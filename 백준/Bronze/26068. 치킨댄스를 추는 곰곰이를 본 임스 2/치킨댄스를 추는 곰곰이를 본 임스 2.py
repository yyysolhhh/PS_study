N = int(input())
ans = 0
for _ in range(N):
    dday = int(input().split("-")[1])
    if dday <= 90:
        ans += 1
print(ans)