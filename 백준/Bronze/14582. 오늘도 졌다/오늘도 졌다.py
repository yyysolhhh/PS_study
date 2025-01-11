u = list(map(int, input().split()))
s = list(map(int, input().split()))
score_u, score_s = 0, 0
ans = False
for i, j in zip(u, s):
    score_u += i
    if score_u > score_s:
        ans = True
    score_s += j
print("Yes" if score_u < score_s and ans else "No")