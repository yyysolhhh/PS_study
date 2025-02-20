while True:
    B, N = map(int, input().split())
    if B == N == 0:
        break
    i = 0
    while i ** N < B:
        i += 1
    if i ** N - B > B - (i - 1) ** N:
        A = i - 1
    else:
        A = i
    print(A)