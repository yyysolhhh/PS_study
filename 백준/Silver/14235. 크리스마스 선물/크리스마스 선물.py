import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
gift = []
for _ in range(n):
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        if len(gift):
            print(-heappop(gift))
        else:
            print(-1)
    else:
        for i in nums[1:]:
            heappush(gift, -i)
