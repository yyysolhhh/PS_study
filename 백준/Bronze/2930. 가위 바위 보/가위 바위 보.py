def rsp(s, f):
    if s == "S":
        if f == "S":
            return 1
        elif f == "P":
            return 2
        elif f == "R":
            return 0
    elif s == "P":
        if f == "P":
            return 1
        elif f == "R":
            return 2
        elif f == "S":
            return 0
    elif s == "R":
        if f == "R":
            return 1
        elif f == "S":
            return 2
        elif f == "P":
            return 0

R = int(input())
san = input()
N = int(input())
fri = [input() for _ in range(N)]
ans, best = 0, 0
for k in fri:
    for i, j in zip(san, k):
        ans += rsp(i, j)
for r in range(R):
    s_point, p_point, r_point = 0, 0, 0
    for i in range(N):
        s_point += rsp("S", fri[i][r])
        p_point += rsp("P", fri[i][r])
        r_point += rsp("R", fri[i][r])
    best += max(s_point, p_point, r_point)
print(ans)
print(best)