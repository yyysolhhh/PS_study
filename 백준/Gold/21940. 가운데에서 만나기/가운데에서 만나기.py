from sys import stdin, maxsize

def solution(N,edges,K,C):
    answer = []

    graph = [[maxsize] * (N+1) for _ in range(N+1)]
    for A, B, T in edges:
        graph[A][B] = T
    for i in range(1,N+1):
        graph[i][i] = 0

    for k in range(1,N+1):
        for j in range(1,N+1):
            for i in range(1,N+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    
    cities = [0] * (N+1)
    for X in range(1, N+1):
        maxValue = 0
        for c in C:
            if c == X or graph[c][X] == maxsize or graph[X][c] == maxsize: continue
            maxValue = max(maxValue, graph[X][c] + graph[c][X])
        cities[X] = maxValue
    
    target = min(cities[1:])
    for X in range(1,N+1):
        if cities[X] == target:
            answer.append(X)
    
    return answer

N, M = map(int,stdin.readline().split())
edges = list(tuple(map(int,stdin.readline().split())) for _ in range(M))
K = int(stdin.readline())
C = list(map(int,stdin.readline().split()))

result = solution(N,edges,K,C)
print(*result)