import sys
input = sys.stdin.readline
N, M = map(int, input().split())
P = []
for _ in range(M):
    P.append(int(input()))
prices = sorted(P, reverse = True)
profit = 0
for i, p in enumerate(prices, start=1):
    i = min(N, i)
    temp = p * i
    if profit < temp:
        profit = temp
        fixed_p = p
print(fixed_p, profit)