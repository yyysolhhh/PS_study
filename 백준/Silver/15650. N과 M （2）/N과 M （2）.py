def series():
    if len(combi) == M:
        print(' '.join(map(str, combi)))
        return
    for i in range(1, N+1):
        if combi:
            if i in combi or i <= combi[-1]:
                continue
        combi.append(i)
        series()
        combi.pop()
N, M = map(int, input().split())
combi = []
series()
