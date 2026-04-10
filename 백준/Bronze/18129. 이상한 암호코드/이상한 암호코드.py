S, K = input().split()
K = int(K)
S = S.upper()
alpha = [S[0]]
cnt = [1]
for i in range(1, len(S)):
    if S[i] == S[i - 1]:
        if S[i] != alpha[-1]:
            continue
        cnt[-1] += 1
    else:
        if S[i] in alpha:
            continue
        alpha.append(S[i])
        cnt.append(1)
for i in cnt:
    if i >= K:
        print(1, end="")
    else:
        print(0, end="")
