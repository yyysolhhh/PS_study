A, B = map(int, input().split())
K, X = map(int, input().split())
s, e = 0, 0
if K + X < A or K - X > B:
    print("IMPOSSIBLE")
else:
    if K - X < A < K + X:
        s = A
    elif K - X > A:
        s = K - X
    if K - X < B < K + X:
        e = B
    elif K + X < B:
        e = K + X
    print(e - s + 1)