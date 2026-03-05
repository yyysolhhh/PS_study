import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    M, N = map(int, input().split())
    nums = [list(map(int, input().split())) for _ in range(N)]
    mx = -float('inf')
    ans = 0
    for i in range(M):
        mul = 1
        for j in range(N):
            mul *= nums[j][i]
        if mx <= mul:
            mx = mul
            ans = i + 1
    print(ans)