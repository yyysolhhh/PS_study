N, K = map(int, input().split())
nums = []
fK = K % 10
fK2 = 2 * K % 10
for i in range(1, N + 1):
    if i % 10 != fK and i % 10 != fK2:
        nums.append(i)
print(len(nums))
print(*nums)