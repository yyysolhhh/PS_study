import sys
input = sys.stdin.readline
T = int(input())
mod = 1000000009
dp = [[0] * 4 for _ in range(100001)]
dp[1] = [0, 1, 0, 0]
dp[2] = [0, 0, 1, 0]
dp[3] = [0, 1, 1, 1]
for i in range(4, 100001):
    for j in range(1, 4):
        dp[i][j] = (dp[i-j][1] + dp[i-j][2] + dp[i-j][3] - dp[i-j][j]) % mod
for _ in range(T):
    n = int(input())
    print(sum(dp[n]) % mod)