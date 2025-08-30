N, E = map(int, input().split())
D = sorted(map(int, input().split()))
ans = 1
for i in range(N - 1):
    if D[i + 1] - D[i] >= E:
        ans += 1
print(ans)