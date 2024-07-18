import sys
input = sys.stdin.readline
N, M = map(int, input().split())
num = list(map(int, input().split()))
acc_sum = [0, num[0]]
for i in range(2, N+1):
    acc_sum.append(acc_sum[i-1] + num[i-1])
for _ in range(M):
    i, j = map(int, input().split())
    print(acc_sum[j] - acc_sum[i-1])