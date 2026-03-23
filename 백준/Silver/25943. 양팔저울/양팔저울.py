n = int(input())
nums = list(map(int, input().split()))
w = [100, 50, 20, 10, 5, 2, 1]
left, right = nums[0], nums[1]
for i in nums[2:]:
    if left <= right:
        left += i
    else:
        right += i
diff = abs(left - right)
ans = 0
while diff > 0:
    for i in w:
        ans += diff // i
        diff %= i
print(ans)
