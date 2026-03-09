cards = list(map(int, input().split()))
nums = [1 for _ in range(10)]
ans = 6
for i in cards:
    nums[i] = 0
for i in range(6):
    tmp = sum(nums[i:i + 5])
    if tmp < ans:
        ans = tmp
print(ans)
