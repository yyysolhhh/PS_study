ans = 0
A = [0]
N = int(input())
for _ in range(N):
    A.append(int(input()))
M = int(input())
for _ in range(M):
    B = int(input())
    ans += A[B]
print(ans)