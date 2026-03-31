A, B, K = map(int, input().split())
candi = []
ans = [A, B]
for i in range(A, B + 1, A):
    if B % i == 0:
        candi.append(i)
if len(candi) < K:
    print(-1)
else:
    ans.extend(candi[1:K - 1])
    print(*ans)
