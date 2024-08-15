import sys
input = sys.stdin.readline
N = int(input())
nums = set(map(int, input().split()))
print(*sorted(nums))