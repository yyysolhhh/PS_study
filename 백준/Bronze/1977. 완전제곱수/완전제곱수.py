M = int(input())
N = int(input())
nums = []
for i in range(M, N + 1):
    if i ** 0.5 == int(i ** 0.5):
        nums.append(i)
if len(nums) == 0:
    print(-1)
else:
    print(sum(nums))
    print(min(nums))