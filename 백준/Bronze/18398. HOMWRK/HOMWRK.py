T = int(input())
for _ in range(T):
    n = int(input())
    for _ in range(n):
        A, B = map(int, input().split())
        print(A + B, A * B)