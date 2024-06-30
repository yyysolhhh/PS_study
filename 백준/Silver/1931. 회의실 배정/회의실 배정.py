N = int(input())
info = []
for _ in range(N):
    start, end = map(int, input().split())
    info.append([start, end])
info.sort(key=lambda x: (x[1], x[0]))
pre = 0
cnt = 0
for i in range(N):
    if info[i][0] >= pre:
        pre = info[i][1]
        cnt += 1
print(cnt)
