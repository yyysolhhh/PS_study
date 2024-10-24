N = int(input())
if N == 1:
    print(1)
elif N % 2:
    if N // 2 % 2 == 0:
        print(N - 1)
    else:
        print(N // 2 + 1)
else:
    print(N)