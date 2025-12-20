import sys
input = sys.stdin.readline
N = int(input())
inout = set()
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b == 1:
        if a in inout:
            ans += 1
        else:
            inout.add(a)
    else:
        if a not in inout:
            ans += 1
        else:
            inout.remove(a)
ans += len(inout)
print(ans)