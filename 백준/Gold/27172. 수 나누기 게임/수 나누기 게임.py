import sys
input = sys.stdin.readline

N = int(input())
x = list(map(int, input().rstrip().split()))
S = set(x)
M = max(x)
sieve = [0 for _ in range(M+1)]
for i in x:
    if i == M: continue
    for j in range(2*i, M+1, i):
        if j in S:
            sieve[i] += 1
            sieve[j] -= 1
for i in x:
    print(sieve[i], end = ' ')