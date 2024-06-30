import sys
input = sys.stdin.readline
N = int(input())
P = [0] + list(map(int, input().split()))
dp = [0 for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, i+1):
        if dp[i] != 0:
            dp[i] = min(dp[i], P[j] + dp[i-j])
        else:
            dp[i] = P[j] + dp[i-j]
print(dp[N])