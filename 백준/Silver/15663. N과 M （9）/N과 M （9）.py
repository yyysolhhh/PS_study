from itertools import permutations
N, M = map(int, input().split())
nums = sorted(map(int, input().split()))
perms = sorted(set(permutations(nums, M)))
for i in perms:
    print(*i)