def solve(postit):
    j = 0
    for i in postit:
        if i == S[j]:
            j += 1
            if j == len(S):
                return True
    return False
N, M = map(int, input().split())
S = input()
for _ in range(M):
    postit = input()
    if solve(postit):
        print("true")
    else:
        print("false")