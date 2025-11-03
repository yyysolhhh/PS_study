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
AB = [a + b for a in A for b in B]
CD = Counter([c + d for c in C for d in D])
for i in AB:
    ans += CD[-i]
print(ans)