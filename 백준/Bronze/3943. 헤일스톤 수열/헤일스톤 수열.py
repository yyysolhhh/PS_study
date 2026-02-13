import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    nums = [n]
    last = n
    while last != 1:
        if last & 1 == 1:
            last = last * 3 + 1
        else:
            last //= 2
        nums.append(last)
    print(max(nums))