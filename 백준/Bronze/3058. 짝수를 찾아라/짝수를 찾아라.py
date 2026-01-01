T = int(input())
for _ in range(T):
    nums = list(map(int, input().split()))
    tot = 0
    ans = 101
    for i in nums:
        if i & 1 == 0:
            tot += i
            if i < ans:
                ans = i
    print(tot, ans)