import sys
input = sys.stdin.readline
for _ in range(3):
    N = int(input())
    nums = [int(input()) for _ in range(N)]
    S = sum(nums)
    if S > 0:
        print("+")
    elif S < 0:
        print("-")
    else:
        print(0)