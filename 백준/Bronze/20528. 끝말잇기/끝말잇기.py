N = int(input())
S = list(input().split())
ans = 1
for i in S[1:]:
    if i[0] != S[0][0]:
        ans = 0
        break
print(ans)