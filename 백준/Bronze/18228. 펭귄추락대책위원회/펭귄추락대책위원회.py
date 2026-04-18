N = int(input())
A = list(map(int, input().split()))
for i, j in enumerate(A):
    if j == -1:
        p = i
print(min(A[:p]) + min(A[p + 1:]))
