from itertools import permutations
N, M = map(int, input().split())
perm = list(permutations(range(1, N+1), M))
for i in perm:
    print(*i)