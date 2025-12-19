import sys
input = sys.stdin.readline
H, x = map(int, input().split())
C = int(1e9 + 7)
div = 1
ans = 0
for _ in range(H):
    div *= x
    div %= C
    ans += int(input()) * div
    ans %= C
print(ans)