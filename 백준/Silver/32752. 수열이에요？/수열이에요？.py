N, L, R = map(int, input().split())
A = list(map(int, input().split()))
A[L - 1:R] = sorted(A[L - 1:R])
print(int(all(A[i] <= A[i + 1] for i in range(N - 1))))