import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
for i in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
ans = 0
AB = sorted(a + b for a in A for b in B)
CD = sorted(c + d for c in C for d in D)
ab, cd = 0, len(CD) - 1
while ab < len(AB) and cd >= 0:
    tot = AB[ab] + CD[cd]
    if tot == 0:
        cur_ab = ab
        cur_cd = cd
        ab_cnt = 0
        while ab < len(AB) and AB[ab] == AB[cur_ab]:
            ab += 1
            ab_cnt += 1
        cd_cnt = 0
        while cd >= 0 and CD[cd] == CD[cur_cd]:
            cd -= 1
            cd_cnt += 1
        ans += ab_cnt * cd_cnt
    elif tot < 0:
        ab += 1
    else:
        cd -= 1
print(ans)