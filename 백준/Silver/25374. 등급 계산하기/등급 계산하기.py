N = int(input())
A = sorted(map(int, input().split()), reverse=True)
rate = [0.04, 0.11, 0.23, 0.40, 0.60, 0.77, 0.89, 0.96]
boundary = [A[int(N * i) - 1] for i in rate] + [0]
ans = [0 for _ in range(9)]
idx = 0
for i in range(9):
    cnt = 0
    while idx < N and A[idx] >= boundary[i]:
        idx += 1
        cnt += 1
    ans[i] += cnt
for i in ans:
    print(i)
