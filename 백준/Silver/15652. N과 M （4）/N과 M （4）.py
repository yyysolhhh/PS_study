def series(start):
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(start, N+1):
        combi.append(i)
        series(i)
        combi.pop()
N, M = map(int, input().split())
combi = []
series(1)
