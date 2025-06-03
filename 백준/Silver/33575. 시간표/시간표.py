import sys
input = sys.stdin.readline
N, M, A, B = map(int, input().split())
T = list(map(int, input().split()))
L = list(map(int, input().split()))
H = list(map(int, input().split()))
like = [0 for _ in range(M + 1)]
ans = 0
for i in L:
    like[i] = 1
for i in H:
    like[i] = -1
cnt = like[T[0]]
for i in range(1, N):
    if like[T[i]] != like[T[i - 1]]:
        if abs(cnt) >= 3:
            ans += cnt
        cnt = 0
    cnt += like[T[i]]
if abs(cnt) >= 3:
    ans += cnt
print(ans)