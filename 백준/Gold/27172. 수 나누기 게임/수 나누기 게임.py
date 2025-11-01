import sys
input = sys.stdin.readline
N = int(input())
x = list(map(int, input().split()))
set_x = set(x)
max_x = max(x)
scores = [0 for _ in range(max_x + 1)]
for i in x:
    for j in range(i * 2, max_x + 1, i):
        if j in set_x:
            scores[i] += 1
            scores[j] -= 1
for i in x:
    print(scores[i], end=" ")