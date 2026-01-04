import sys
input = sys.stdin.readline
N, M = map(int, input().split())
stds = [[] for i in range(N + 1)]
while True:
    c, n = input().strip().split()
    if c == '0' and n == '0':
        break
    c = int(c)
    if c > N:
        continue
    if len(stds[c]) < M:
        stds[c].append(n)
for lst in stds:
    lst.sort()
    lst.sort(key=lambda x: len(x))
for cls, lst in enumerate(stds[1:], start=1):
    if cls & 1 == 1:
        for name in lst:
            print(cls, name)
for cls, lst in enumerate(stds[1:], start=1):
    if cls & 1 == 0:
        for name in lst:
            print(cls, name)