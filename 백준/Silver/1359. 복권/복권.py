from itertools import combinations
N, M, K = map(int, input().split())
nums = [i for i in range(1, N + 1)]
comb = list(combinations(nums, M))
ans = 0
for i in comb:
    cnt = 0
    for j in range(M):
        if i[j] <= M:
            cnt += 1
    if cnt >= K:
        ans += 1
print(ans / len(comb))