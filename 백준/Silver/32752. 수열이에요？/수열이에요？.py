N, L, R = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
A = A[:L - 1] + sorted(A[L - 1:R]) + A[R:]
for i in range(N - 1):
    if A[i] > A[i + 1]:
        ans = 0
        break
print(ans)