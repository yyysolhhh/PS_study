import sys
input = sys.stdin.readline
N, M = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(N)]
res = []
for c1 in range(0, M - 2):
    for c2 in range(c1 + 1, M - 1):
        for c3 in range(c2 + 1, M):
            temp = 0
            for i in a:
                temp += max(i[c1], i[c2], i[c3])
            res.append(temp)
print(max(res))