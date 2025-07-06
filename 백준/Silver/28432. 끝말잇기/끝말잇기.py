N = int(input())
S = [input() for _ in range(N)]
M = int(input())
A = [input() for _ in range(M)]
if N == 1:
    print(A[0])
else:
    loc = S.index("?")
    for i in range(M):
        if A[i] in S:
            continue
        if loc == 0:
            if A[i][-1] == S[1][0]:
                print(A[i])
        elif loc == N - 1:
            if A[i][0] == S[N - 2][-1]:
                print(A[i])
        else:
            if A[i][-1] == S[loc + 1][0] and A[i][0] == S[loc - 1][-1]:
                print(A[i])