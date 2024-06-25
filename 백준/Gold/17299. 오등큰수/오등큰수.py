import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
stack = []
F = Counter(A)
NGF = [-1 for _ in range(N)]
for i in range(N):
    while stack and F[A[stack[-1]]] < F[A[i]]:
        NGF[stack.pop()] = A[i]
    stack.append(i)
print(*NGF)
