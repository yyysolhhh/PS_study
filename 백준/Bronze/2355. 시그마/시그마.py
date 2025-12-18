def total(n):
    return (1 + n) * n // 2

A, B = map(int, input().split())
if A > B:
    A, B = B, A
print(total(B) - total(A) + A)