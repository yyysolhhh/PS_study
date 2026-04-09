import sys
input = sys.stdin.readline
n = int(input())
nums = list(map(int, input().split()))
min_n = min(nums)
for i in range(1, min_n + 1):
    cnt = 0
    for j in nums:
        if j % i == 0:
            cnt += 1
    if cnt == n:
        print(i)
