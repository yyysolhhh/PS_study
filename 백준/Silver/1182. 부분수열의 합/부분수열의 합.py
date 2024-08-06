from itertools import combinations
N, S = map(int, input().split())
num = list(map(int, input().split()))
res = 0
for i in range(1, N+1):
    combi = list(combinations(num, i))
    for j in combi:
        if sum(j) == S:
            res += 1
print(res)