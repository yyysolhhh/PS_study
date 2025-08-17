def print_cnt(S, l, r):
    cnt = 1
    for i in range(l, r):
        if S[i] != S[i + 1]:
            cnt += 1
    return cnt

def alter_alpha(S, l, r):
    res = list(S)
    for i in range(l, r + 1):
        if res[i] == "Z":
            res[i] = "A"
        else:
            res[i] = chr(ord(res[i]) + 1)
    return "".join(res)

N, Q = map(int, input().split())
S = input()
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        print(print_cnt(S, query[1] - 1, query[2] - 1))
    elif query[0] == 2:
        S = alter_alpha(S, query[1] - 1, query[2] - 1)