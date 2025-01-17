A, B = map(int, input().split())
print(A // B, end=".")
if A % B:
    for i in range(1000):
        A = A % B * 10
        print(A // B, end="")