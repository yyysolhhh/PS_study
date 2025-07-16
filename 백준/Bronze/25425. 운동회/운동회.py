N, M, a, K = map(int, input().split())
print(min(a-K+1, N), (a-K)//M + ((a-K)%M != 0) + 1)