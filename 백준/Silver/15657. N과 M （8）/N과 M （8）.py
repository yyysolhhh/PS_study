def series(start):
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(start, len(num)):
        combi.append(num[i])
        series(i)
        combi.pop()
N, M = map(int, input().split())
num = sorted(map(int, input().split()))
combi = []
series(0)
