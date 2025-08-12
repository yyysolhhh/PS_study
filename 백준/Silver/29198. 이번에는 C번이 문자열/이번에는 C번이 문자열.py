N, M, K = map(int, input().split())
S = [sorted(input()) for _ in range(N)]
S.sort()
ans = ""
for i in S[:K]:
    ans += "".join(i)
print("".join(sorted(ans)))