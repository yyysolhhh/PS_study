N = int(input())
profits = list(map(int, input().split()))
prices = list(map(int, input().split()))
best = max(profits)
for i in range(N):
    if profits[i] == best:
        print(profits[i] - sorted(profits)[-2], end=" ")
    else:
        print(profits[i] - best, end=" ")