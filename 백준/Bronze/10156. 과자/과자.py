K, N, M = map(int, input().split())
ans = K * N - M
print(ans if ans > 0 else 0)