def gcd(A, B):
    while B:
        A, B = B, A % B
    return A * '1'
A, B = map(int, input().split())
print(gcd(A, B))