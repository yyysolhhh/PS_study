n = int(input())
theta = list(map(int, input().split()))
print(180 * (n - 1) - sum(theta) * 2)