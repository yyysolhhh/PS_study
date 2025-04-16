x0, N = map(int, input().split())
nx = x0
for i in range(1, N + 1):
    if nx % 2 == 0:
        nx = (nx // 2) ^ 6
    else:
        nx = (2 * nx) ^ 6
print(nx)