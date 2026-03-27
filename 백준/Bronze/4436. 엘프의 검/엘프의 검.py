import sys
input = sys.stdin.readline
while True:
    try:
        n = int(input())
    except Exception:
        break
    nums = set()
    k = 1
    while True:
        cur = n * k
        for i in str(cur):
            nums.add(i)
        if len(nums) == 10:
            break
        k += 1
    print(k)
    