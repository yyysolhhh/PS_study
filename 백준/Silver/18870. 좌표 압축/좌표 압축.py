import sys
input = sys.stdin.readline
N = int(input())
X = list(map(int, input().split()))
Xs = sorted(set(X))
Xp = {Xs[i]: i for i in range(len(Xs))}
for i in X:
    print(Xp[i], end=' ')
