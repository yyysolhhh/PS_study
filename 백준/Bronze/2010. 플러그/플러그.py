import sys
input = sys.stdin.readline
N = int(input())
ans = 0
for i in range(N):
    plug = int(input())
    if i == N - 1:
        ans += plug
    else:
        ans += plug - 1
print(ans)