N = int(input())
line = [0 for _ in range(10001)]
for _ in range(N):
    X, Y = map(int, input().split())
    for i in range(X, Y):
        line[i] = 1
print(sum(line))