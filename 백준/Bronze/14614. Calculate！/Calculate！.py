A, B, C = map(int, input().split())
for _ in range(C % 2):
    A ^= B
print(A)