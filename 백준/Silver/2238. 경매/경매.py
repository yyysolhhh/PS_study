U, N = map(int, input().split())
arr = [[] for _ in range(U + 1)]
for _ in range(N):
    S, P = input().split()
    arr[int(P)].append(S)
min_num = N
for i in range(U + 1):
    if (len(arr[i]) != 0):
        min_num = min(min_num, len(arr[i]))
for i in range(U + 1):
    if len(arr[i]) == min_num:
        print(arr[i][0], i)
        break