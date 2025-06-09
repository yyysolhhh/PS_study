N, K = map(int, input().split())
A = list(map(int, input().split()))
print(sorted(A)[K - 1])