N, nK = map(int, input().split())
K = list(map(int, input().split()))
for i in range(N, 0, -1):
    if all(int(j) in K for j in str(i)):
        print(i)
        break