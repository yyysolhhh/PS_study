def stars(x):
    global Map
    if x == 3:
        for _ in range(x):
            for i in range(3):
                for j in range(3):
                    if (i == 1 and j == 1):
                        continue
                    else:
                        Map[i][j] = 1
        return Map
    a = x // 3
    stars(a)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                Map[a*i+k][a*j:a*(j+1)] = Map[k][:a]
N = int(input())
Map = [[0 for _ in range(N)] for _ in range(N)]
stars(N)
for i in Map:
    for j in i:
        if j == 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()