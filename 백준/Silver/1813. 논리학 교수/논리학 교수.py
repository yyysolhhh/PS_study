N = int(input())
nums = list(map(int, input().split()))
ans = -1
for i in range(N + 1):
    cnt = nums.count(i)
    if i == cnt:
        ans = max(ans, cnt)
print(ans)