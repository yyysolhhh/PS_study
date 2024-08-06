def series():
    if len(combi) == M:
        print(" ".join(map(str, combi)))
        return
    for i in num:
        if i in combi:
            continue
        combi.append(i)
        series()
        combi.pop()
N, M = map(int, input().split())
num = list(map(int, input().split()))
num.sort()
combi = []
series()
