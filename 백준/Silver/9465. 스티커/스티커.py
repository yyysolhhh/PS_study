import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    dp = [[0 for _ in range(n)] for _ in range(2)]
    stickers = []
    for _ in range(2):
        stickers.append(list(map(int, input().split())))
    for j in range(n):
        for i in range(2):
            v = 0
            if j > 1:
                v = max(dp[0][j - 2], dp[1][j - 2])
            if j > 0:
                v = max(v, dp[1 - i][j - 1])
            dp[i][j] = v + stickers[i][j]
    print(max(dp[0][n - 1], dp[1][n - 1]))