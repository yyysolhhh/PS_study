N = int(input())
print("Gnomes:")
for _ in range(N):
    nums = list(map(int, input().split()))
    if nums == sorted(nums) or nums == sorted(nums, reverse=True):
        print("Ordered")
    else:
        print("Unordered")