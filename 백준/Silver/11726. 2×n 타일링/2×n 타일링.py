n = int(input())
dp = [1, 2]
if n == 1:
  print(dp[0] % 10007)
elif n == 2:
  print(dp[1] % 10007)
else:
  for i in range(2, n):
    dp.append(dp[i-1] + dp[i-2])
  print(dp[-1] % 10007)
