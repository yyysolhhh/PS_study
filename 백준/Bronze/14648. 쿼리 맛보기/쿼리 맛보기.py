n, q = map(int, input().split())
nums = list(map(int, input().split()))
for _ in range(q):
    query = list(map(int, input().split()))
    a, b = query[1] - 1, query[2] - 1
    if query[0] == 1:
        print(sum(nums[a:b + 1]))
        nums[a], nums[b] = nums[b], nums[a]
    elif query[0] == 2:
        c, d = query[3] - 1, query[4] - 1
        print(sum(nums[a:b + 1]) - sum(nums[c:d + 1]))
