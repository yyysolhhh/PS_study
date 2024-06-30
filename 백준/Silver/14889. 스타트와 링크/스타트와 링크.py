import sys
from itertools import combinations
input = sys.stdin.readline
N = int(input())

# 1 틀림
# S = []
# S_pair = []
# gap = set()
# for _ in range(N):
#     S.append(list(map(int, input().split())))
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             break
#         S_pair.append(S[i][j] + S[j][i])
# combi = set(map(sum, (list(set(combinations(S_pair, N//2))))))
# for i in combi:
#   gap.add(abs(i[0] - i[1]))
# print(min(gap))
S = [i for i in range(N)]
case = list(combinations(S, N//2))
for i in range(N):
    S[i] = list(map(int, input().split()))

result = 100
for c1 in case:
    team_start = 0
    team_link = 0
    for i in c1:
        for j in c1:
            team_start += S[i][j]
    c2 = [i for i in range(N) if i not in c1]
    for i in c2:
        for j in c2:
            team_link += S[i][j]
    result = min(result, abs(team_start - team_link))
print(result)