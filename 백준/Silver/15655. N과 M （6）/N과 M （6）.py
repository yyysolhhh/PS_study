def series(start):
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(start, len(num)):
        combi.append(num[i])
        series(i+1)
        combi.pop()
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
combi = []
series(0)
