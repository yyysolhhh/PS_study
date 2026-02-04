T, X = map(int, input().split())
N = int(input())
ans = "YES"
for _ in range(N):
    K = int(input())
    A = list(map(int, input().split()))
    if X not in A:
        ans = "NO"
print(ans)