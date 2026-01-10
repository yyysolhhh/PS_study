N, X = map(int, input().split())
A = list(map(int, input().split()))
ans = []
for i in range(N - 1):
    ans.append((A[i] + A[i + 1]) * X)
print(min(ans))