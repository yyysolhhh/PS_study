import sys
input = sys.stdin.readline
N = int(input())
inout = {}
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if a in inout:
        if inout[a] == 1:
            if b == 1:
                ans += 1
        else:
            if b == 0:
                ans += 1
    else:
        if b == 0:
            ans += 1
    inout[a] = b
for _, v in inout.items():
    if v == 1:
        ans += 1
print(ans)